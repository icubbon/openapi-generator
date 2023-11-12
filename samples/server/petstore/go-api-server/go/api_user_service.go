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
	"context"
	"net/http"
	"errors"
)

// UserAPIService is a service that implements the logic for the UserAPIServicer
// This service should implement the business logic for every endpoint for the UserAPI API.
// Include any external packages or services that will be required by this service.
type UserAPIService struct {
}

// NewUserAPIService creates a default api service
func NewUserAPIService() UserAPIServicer {
	return &UserAPIService{}
}

// CreateUser - Create user
func (s *UserAPIService) CreateUser(ctx context.Context, user User) (ImplResponse, error) {
	// TODO - update CreateUser with the required logic for this service method.
	// Add api_user_service.go to the .openapi-generator-ignore to avoid overwriting this service implementation when updating open api generation.

	// TODO: Uncomment the next line to return response Response(0, {}) or use other options such as http.Ok ...
	// return Response(0, nil),nil

	return Response(http.StatusNotImplemented, nil), errors.New("CreateUser method not implemented")
}

// CreateUsersWithArrayInput - Creates list of users with given input array
func (s *UserAPIService) CreateUsersWithArrayInput(ctx context.Context, user []User) (ImplResponse, error) {
	// TODO - update CreateUsersWithArrayInput with the required logic for this service method.
	// Add api_user_service.go to the .openapi-generator-ignore to avoid overwriting this service implementation when updating open api generation.

	// TODO: Uncomment the next line to return response Response(0, {}) or use other options such as http.Ok ...
	// return Response(0, nil),nil

	return Response(http.StatusNotImplemented, nil), errors.New("CreateUsersWithArrayInput method not implemented")
}

// CreateUsersWithListInput - Creates list of users with given input array
func (s *UserAPIService) CreateUsersWithListInput(ctx context.Context, user []User) (ImplResponse, error) {
	// TODO - update CreateUsersWithListInput with the required logic for this service method.
	// Add api_user_service.go to the .openapi-generator-ignore to avoid overwriting this service implementation when updating open api generation.

	// TODO: Uncomment the next line to return response Response(0, {}) or use other options such as http.Ok ...
	// return Response(0, nil),nil

	return Response(http.StatusNotImplemented, nil), errors.New("CreateUsersWithListInput method not implemented")
}

// DeleteUser - Delete user
func (s *UserAPIService) DeleteUser(ctx context.Context, username string, booleanTest *bool) (ImplResponse, error) {
	// TODO - update DeleteUser with the required logic for this service method.
	// Add api_user_service.go to the .openapi-generator-ignore to avoid overwriting this service implementation when updating open api generation.

	// TODO: Uncomment the next line to return response Response(400, {}) or use other options such as http.Ok ...
	// return Response(400, nil),nil

	// TODO: Uncomment the next line to return response Response(404, {}) or use other options such as http.Ok ...
	// return Response(404, nil),nil

	return Response(http.StatusNotImplemented, nil), errors.New("DeleteUser method not implemented")
}

// GetUserByName - Get user by user name
func (s *UserAPIService) GetUserByName(ctx context.Context, username string) (ImplResponse, error) {
	// TODO - update GetUserByName with the required logic for this service method.
	// Add api_user_service.go to the .openapi-generator-ignore to avoid overwriting this service implementation when updating open api generation.

	// TODO: Uncomment the next line to return response Response(200, User{}) or use other options such as http.Ok ...
	// return Response(200, User{}), nil

	// TODO: Uncomment the next line to return response Response(400, {}) or use other options such as http.Ok ...
	// return Response(400, nil),nil

	// TODO: Uncomment the next line to return response Response(404, {}) or use other options such as http.Ok ...
	// return Response(404, nil),nil

	return Response(http.StatusNotImplemented, nil), errors.New("GetUserByName method not implemented")
}

// LoginUser - Logs user into the system
func (s *UserAPIService) LoginUser(ctx context.Context, username string, password string, booleanTest *bool) (ImplResponse, error) {
	// TODO - update LoginUser with the required logic for this service method.
	// Add api_user_service.go to the .openapi-generator-ignore to avoid overwriting this service implementation when updating open api generation.

	// TODO: Uncomment the next line to return response Response(200, string{}) or use other options such as http.Ok ...
	// return Response(200, string{}), nil

	// TODO: Uncomment the next line to return response Response(400, {}) or use other options such as http.Ok ...
	// return Response(400, nil),nil

	return Response(http.StatusNotImplemented, nil), errors.New("LoginUser method not implemented")
}

// LogoutUser - Logs out current logged in user session
func (s *UserAPIService) LogoutUser(ctx context.Context) (ImplResponse, error) {
	// TODO - update LogoutUser with the required logic for this service method.
	// Add api_user_service.go to the .openapi-generator-ignore to avoid overwriting this service implementation when updating open api generation.

	// TODO: Uncomment the next line to return response Response(0, {}) or use other options such as http.Ok ...
	// return Response(0, nil),nil

	return Response(http.StatusNotImplemented, nil), errors.New("LogoutUser method not implemented")
}

// UpdateUser - Updated user
func (s *UserAPIService) UpdateUser(ctx context.Context, username string, user User) (ImplResponse, error) {
	// TODO - update UpdateUser with the required logic for this service method.
	// Add api_user_service.go to the .openapi-generator-ignore to avoid overwriting this service implementation when updating open api generation.

	// TODO: Uncomment the next line to return response Response(400, {}) or use other options such as http.Ok ...
	// return Response(400, nil),nil

	// TODO: Uncomment the next line to return response Response(404, {}) or use other options such as http.Ok ...
	// return Response(404, nil),nil

	return Response(http.StatusNotImplemented, nil), errors.New("UpdateUser method not implemented")
}
