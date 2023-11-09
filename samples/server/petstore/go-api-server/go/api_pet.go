/*
 * OpenAPI Petstore
 *
 * This is a sample server Petstore server. For this sample, you can use the api key `special-key` to test the authorization filters.
 *
 * API version: 1.0.0
 * Generated by: OpenAPI Generator (https://openapi-generator.tech)
 */

package petstoreserver

import (
	"encoding/json"
	"net/http"
	"strings"

	"github.com/gorilla/mux"
)

// PetAPIController binds http requests to an api service and writes the service results to the http response
type PetAPIController struct {
	service      PetAPIServicer
	errorHandler ErrorHandler
}

// PetAPIOption for how the controller is set up.
type PetAPIOption func(*PetAPIController)

// WithPetAPIErrorHandler inject ErrorHandler into controller
func WithPetAPIErrorHandler(h ErrorHandler) PetAPIOption {
	return func(c *PetAPIController) {
		c.errorHandler = h
	}
}

// NewPetAPIController creates a default api controller
func NewPetAPIController(s PetAPIServicer, opts ...PetAPIOption) Router {
	controller := &PetAPIController{
		service:      s,
		errorHandler: DefaultErrorHandler,
	}

	for _, opt := range opts {
		opt(controller)
	}

	return controller
}

// Routes returns all the api routes for the PetAPIController
func (c *PetAPIController) Routes() Routes {
	return Routes{
		"AddPet": Route{
			strings.ToUpper("Post"),
			"/v2/pet",
			c.AddPet,
		},
		"DeletePet": Route{
			strings.ToUpper("Delete"),
			"/v2/pet/{petId}",
			c.DeletePet,
		},
		"FilterPetsByCategory": Route{
			strings.ToUpper("Get"),
			"/v2/pet/filterPets/{gender}",
			c.FilterPetsByCategory,
		},
		"FindPetsByStatus": Route{
			strings.ToUpper("Get"),
			"/v2/pet/findByStatus",
			c.FindPetsByStatus,
		},
		"FindPetsByTags": Route{
			strings.ToUpper("Get"),
			"/v2/pet/findByTags",
			c.FindPetsByTags,
		},
		"GetPetById": Route{
			strings.ToUpper("Get"),
			"/v2/pet/{petId}",
			c.GetPetById,
		},
		"GetPetImageById": Route{
			strings.ToUpper("Get"),
			"/v2/pet/{petId}/uploadImage",
			c.GetPetImageById,
		},
		"GetPetsUsingBooleanQueryParameters": Route{
			strings.ToUpper("Get"),
			"/v2/pets/boolean/parsing",
			c.GetPetsUsingBooleanQueryParameters,
		},
		"UpdatePet": Route{
			strings.ToUpper("Put"),
			"/v2/pet",
			c.UpdatePet,
		},
		"UpdatePetWithForm": Route{
			strings.ToUpper("Post"),
			"/v2/pet/{petId}",
			c.UpdatePetWithForm,
		},
		"UploadFile": Route{
			strings.ToUpper("Post"),
			"/v2/pet/{petId}/uploadImage",
			c.UploadFile,
		},
		"UploadFileArrayOfFiles": Route{
			strings.ToUpper("Post"),
			"/v2/fake/uploadImage/array of_file",
			c.UploadFileArrayOfFiles,
		},
	}
}

// AddPet - Add a new pet to the store
func (c *PetAPIController) AddPet(w http.ResponseWriter, r *http.Request) {
	petParam := &Pet{}
	d := json.NewDecoder(r.Body)
	d.DisallowUnknownFields()
	if err := d.Decode(petParam); err != nil {
		c.errorHandler(w, r, &ParsingError{Err: err}, nil)
		return
	}
	if err := AssertPetRequired(*petParam); err != nil {
		c.errorHandler(w, r, err, nil)
		return
	}
	if err := AssertPetConstraints(*petParam); err != nil {
		c.errorHandler(w, r, err, nil)
		return
	}
	result, err := c.service.AddPet(r.Context(), *petParam)
	// If an error occurred, encode the error with the status code
	if err != nil {
		c.errorHandler(w, r, err, &result)
		return
	}
	// If no error, encode the body and the result code
	EncodeJSONResponse(result.Body, &result.Code, result.Headers, w)
}

// DeletePet - Deletes a pet
func (c *PetAPIController) DeletePet(w http.ResponseWriter, r *http.Request) {
	params := mux.Vars(r)
	petIdParam, err := parseNumericParameter[int64](
		params["petId"],
		WithRequire[int64](parseInt64),
	)
	if err != nil {
		c.errorHandler(w, r, &ParsingError{Err: err}, nil)
		return
	}
	apiKeyParam := getPointerOrNilIfEmpty(r.Header.Get("api_key"))
	result, err := c.service.DeletePet(r.Context(), *petIdParam, apiKeyParam)
	// If an error occurred, encode the error with the status code
	if err != nil {
		c.errorHandler(w, r, err, &result)
		return
	}
	// If no error, encode the body and the result code
	EncodeJSONResponse(result.Body, &result.Code, result.Headers, w)
}

// FilterPetsByCategory - Finds Pets
func (c *PetAPIController) FilterPetsByCategory(w http.ResponseWriter, r *http.Request) {
	params := mux.Vars(r)
	query := r.URL.Query()
	genderParam, err := NewGenderFromValue(params["gender"])
	if err != nil {
		c.errorHandler(w, r, &ParsingError{Err: err}, nil)
		return
	}
	if !query.Has("species") {
		c.errorHandler(w, r, &RequiredError{"species"}, nil)
		return
	}
	speciesParam, err := NewSpeciesFromValue(query.Get("species"))
	if err != nil {
		c.errorHandler(w, r, &ParsingError{Err: err}, nil)
		return
	}
	var notSpeciesParam []Species
	if query.Has("notSpecies") {
		paramSplits := strings.Split(query.Get("notSpecies"), ",")
		notSpeciesParam = make([]Species, 0, len(paramSplits))
		for _, param := range paramSplits {
			paramEnum, err := NewSpeciesFromValue(param)
			if err != nil {
				c.errorHandler(w, r, &ParsingError{Err: err}, nil)
				return
			}
			notSpeciesParam = append(notSpeciesParam, *paramEnum)
		}
	}
	result, err := c.service.FilterPetsByCategory(r.Context(), *genderParam, *speciesParam, notSpeciesParam)
	// If an error occurred, encode the error with the status code
	if err != nil {
		c.errorHandler(w, r, err, &result)
		return
	}
	// If no error, encode the body and the result code
	EncodeJSONResponse(result.Body, &result.Code, result.Headers, w)
}

// FindPetsByStatus - Finds Pets by status
func (c *PetAPIController) FindPetsByStatus(w http.ResponseWriter, r *http.Request) {
	query := r.URL.Query()
	var statusParam []string
	if query.Has("status") {
		statusParam = strings.Split(query.Get("status"), ",")
	}
	result, err := c.service.FindPetsByStatus(r.Context(), statusParam)
	// If an error occurred, encode the error with the status code
	if err != nil {
		c.errorHandler(w, r, err, &result)
		return
	}
	// If no error, encode the body and the result code
	EncodeJSONResponse(result.Body, &result.Code, result.Headers, w)
}

// FindPetsByTags - Finds Pets by tags
// Deprecated
func (c *PetAPIController) FindPetsByTags(w http.ResponseWriter, r *http.Request) {
	query := r.URL.Query()
	var tagsParam []string
	if query.Has("tags") {
		tagsParam = strings.Split(query.Get("tags"), ",")
	}
	if !query.Has("bornAfter") {
		c.errorHandler(w, r, &RequiredError{"bornAfter"}, nil)
		return
	}
	bornAfterParam, err := parseTime(query.Get("bornAfter"))
	if err != nil {
		c.errorHandler(w, r, &ParsingError{Err: err}, nil)
		return
	}

	bornBeforeParam, err := parseTime(query.Get("bornBefore"))
	if err != nil {
		c.errorHandler(w, r, &ParsingError{Err: err}, nil)
		return
	}

	result, err := c.service.FindPetsByTags(r.Context(), tagsParam, *bornAfterParam, bornBeforeParam)
	// If an error occurred, encode the error with the status code
	if err != nil {
		c.errorHandler(w, r, err, &result)
		return
	}
	// If no error, encode the body and the result code
	EncodeJSONResponse(result.Body, &result.Code, result.Headers, w)
}

// GetPetById - Find pet by ID
func (c *PetAPIController) GetPetById(w http.ResponseWriter, r *http.Request) {
	params := mux.Vars(r)
	petIdParam, err := parseNumericParameter[int64](
		params["petId"],
		WithRequire[int64](parseInt64),
	)
	if err != nil {
		c.errorHandler(w, r, &ParsingError{Err: err}, nil)
		return
	}
	result, err := c.service.GetPetById(r.Context(), *petIdParam)
	// If an error occurred, encode the error with the status code
	if err != nil {
		c.errorHandler(w, r, err, &result)
		return
	}
	// If no error, encode the body and the result code
	EncodeJSONResponse(result.Body, &result.Code, result.Headers, w)
}

// GetPetImageById - Returns the image for the Pet that has been previously uploaded
func (c *PetAPIController) GetPetImageById(w http.ResponseWriter, r *http.Request) {
	params := mux.Vars(r)
	petIdParam, err := parseNumericParameter[int64](
		params["petId"],
		WithRequire[int64](parseInt64),
	)
	if err != nil {
		c.errorHandler(w, r, &ParsingError{Err: err}, nil)
		return
	}
	result, err := c.service.GetPetImageById(r.Context(), *petIdParam)
	// If an error occurred, encode the error with the status code
	if err != nil {
		c.errorHandler(w, r, err, &result)
		return
	}
	// If no error, encode the body and the result code
	EncodeJSONResponse(result.Body, &result.Code, result.Headers, w)
}

// GetPetsUsingBooleanQueryParameters - Get the pets by only using boolean query parameters
func (c *PetAPIController) GetPetsUsingBooleanQueryParameters(w http.ResponseWriter, r *http.Request) {
	query := r.URL.Query()
	exprParam, err := parseBoolParameter(
		query.Get("expr"),
		WithRequire[bool](parseBool),
	)
	if err != nil {
		c.errorHandler(w, r, &ParsingError{Err: err}, nil)
		return
	}
	groupingParam, err := parseBoolParameter(
		query.Get("grouping"),
		WithParse[bool](parseBool),
	)
	if err != nil {
		c.errorHandler(w, r, &ParsingError{Err: err}, nil)
		return
	}
	inactiveParam, err := parseBoolParameter(
		query.Get("inactive"),
		WithDefaultOrParse[bool](false, parseBool),
	)
	if err != nil {
		c.errorHandler(w, r, &ParsingError{Err: err}, nil)
		return
	}
	result, err := c.service.GetPetsUsingBooleanQueryParameters(r.Context(), *exprParam, groupingParam, inactiveParam)
	// If an error occurred, encode the error with the status code
	if err != nil {
		c.errorHandler(w, r, err, &result)
		return
	}
	// If no error, encode the body and the result code
	EncodeJSONResponse(result.Body, &result.Code, result.Headers, w)
}

// UpdatePet - Update an existing pet
func (c *PetAPIController) UpdatePet(w http.ResponseWriter, r *http.Request) {
	petParam := &Pet{}
	d := json.NewDecoder(r.Body)
	d.DisallowUnknownFields()
	if err := d.Decode(petParam); err != nil {
		c.errorHandler(w, r, &ParsingError{Err: err}, nil)
		return
	}
	if err := AssertPetRequired(*petParam); err != nil {
		c.errorHandler(w, r, err, nil)
		return
	}
	if err := AssertPetConstraints(*petParam); err != nil {
		c.errorHandler(w, r, err, nil)
		return
	}
	result, err := c.service.UpdatePet(r.Context(), *petParam)
	// If an error occurred, encode the error with the status code
	if err != nil {
		c.errorHandler(w, r, err, &result)
		return
	}
	// If no error, encode the body and the result code
	EncodeJSONResponse(result.Body, &result.Code, result.Headers, w)
}

// UpdatePetWithForm - Updates a pet in the store with form data
func (c *PetAPIController) UpdatePetWithForm(w http.ResponseWriter, r *http.Request) {
	if err := r.ParseForm(); err != nil {
		c.errorHandler(w, r, &ParsingError{Err: err}, nil)
		return
	}
	params := mux.Vars(r)
	petIdParam, err := parseNumericParameter[int64](
		params["petId"],
		WithRequire[int64](parseInt64),
	)
	if err != nil {
		c.errorHandler(w, r, &ParsingError{Err: err}, nil)
		return
	}

	nameParam := getPointerOrNilIfEmpty(r.FormValue("name"))

	statusParam := getPointerOrNilIfEmpty(r.FormValue("status"))
	result, err := c.service.UpdatePetWithForm(r.Context(), *petIdParam, nameParam, statusParam)
	// If an error occurred, encode the error with the status code
	if err != nil {
		c.errorHandler(w, r, err, &result)
		return
	}
	// If no error, encode the body and the result code
	EncodeJSONResponse(result.Body, &result.Code, result.Headers, w)
}

// UploadFile - uploads an image
func (c *PetAPIController) UploadFile(w http.ResponseWriter, r *http.Request) {
	if err := r.ParseMultipartForm(32 << 20); err != nil {
		c.errorHandler(w, r, &ParsingError{Err: err}, nil)
		return
	}
	params := mux.Vars(r)
	petIdParam, err := parseNumericParameter[int64](
		params["petId"],
		WithRequire[int64](parseInt64),
	)
	if err != nil {
		c.errorHandler(w, r, &ParsingError{Err: err}, nil)
		return
	}

	additionalMetadataParam := getPointerOrNilIfEmpty(r.FormValue("additionalMetadata"))
	fileParam, err := ReadFormFileToTempFile(r, "file")
	if err != nil {
		c.errorHandler(w, r, &ParsingError{Err: err}, nil)
		return
	}

	result, err := c.service.UploadFile(r.Context(), *petIdParam, additionalMetadataParam, fileParam)
	// If an error occurred, encode the error with the status code
	if err != nil {
		c.errorHandler(w, r, err, &result)
		return
	}
	// If no error, encode the body and the result code
	EncodeJSONResponse(result.Body, &result.Code, result.Headers, w)
}

// UploadFileArrayOfFiles - uploads images (array of files)
func (c *PetAPIController) UploadFileArrayOfFiles(w http.ResponseWriter, r *http.Request) {
	if err := r.ParseMultipartForm(32 << 20); err != nil {
		c.errorHandler(w, r, &ParsingError{Err: err}, nil)
		return
	}
	params := mux.Vars(r)
	petIdParam, err := parseNumericParameter[int64](
		params["petId"],
		WithRequire[int64](parseInt64),
	)
	if err != nil {
		c.errorHandler(w, r, &ParsingError{Err: err}, nil)
		return
	}

	additionalMetadataParam := getPointerOrNilIfEmpty(r.FormValue("additionalMetadata"))
	filesParam, err := ReadFormFilesToTempFiles(r, "files")
	if err != nil {
		c.errorHandler(w, r, &ParsingError{Err: err}, nil)
		return
	}

	result, err := c.service.UploadFileArrayOfFiles(r.Context(), *petIdParam, additionalMetadataParam, filesParam)
	// If an error occurred, encode the error with the status code
	if err != nil {
		c.errorHandler(w, r, err, &result)
		return
	}
	// If no error, encode the body and the result code
	EncodeJSONResponse(result.Body, &result.Code, result.Headers, w)
}
