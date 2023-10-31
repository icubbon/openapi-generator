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

// StoreAPIService is a service that implements the logic for the StoreAPIServicer
// This service should implement the business logic for every endpoint for the StoreAPI API.
// Include any external packages or services that will be required by this service.
type StoreAPIService struct {
}

// NewStoreAPIService creates a default api service
func NewStoreAPIService() StoreAPIServicer {
	return &StoreAPIService{}
}

// DeleteOrder - Delete purchase order by ID
func (s *StoreAPIService) DeleteOrder(ctx context.Context, string) (ImplResponse, error) {
	// TODO - update DeleteOrder with the required logic for this service method.
	// Add api_store_service.go to the .openapi-generator-ignore to avoid overwriting this service implementation when updating open api generation.

	// TODO: Uncomment the next line to return response Response(400, {}) or use other options such as http.Ok ...
	// return Response(400, nil),nil

	// TODO: Uncomment the next line to return response Response(404, {}) or use other options such as http.Ok ...
	// return Response(404, nil),nil

	return Response(http.StatusNotImplemented, nil), errors.New("DeleteOrder method not implemented")
}

// GetInventory - Returns pet inventories by status
func (s *StoreAPIService) GetInventory(ctx context.Context) (ImplResponse, error) {
	// TODO - update GetInventory with the required logic for this service method.
	// Add api_store_service.go to the .openapi-generator-ignore to avoid overwriting this service implementation when updating open api generation.

	// TODO: Uncomment the next line to return response Response(200, map[string]int32{}) or use other options such as http.Ok ...
	// return Response(200, map[string]int32{}), nil

	return Response(http.StatusNotImplemented, nil), errors.New("GetInventory method not implemented")
}

// GetOrderById - Find purchase order by ID
func (s *StoreAPIService) GetOrderById(ctx context.Context, int64) (ImplResponse, error) {
	// TODO - update GetOrderById with the required logic for this service method.
	// Add api_store_service.go to the .openapi-generator-ignore to avoid overwriting this service implementation when updating open api generation.

	// TODO: Uncomment the next line to return response Response(200, Order{}) or use other options such as http.Ok ...
	// return Response(200, Order{}), nil

	// TODO: Uncomment the next line to return response Response(400, {}) or use other options such as http.Ok ...
	// return Response(400, nil),nil

	// TODO: Uncomment the next line to return response Response(404, {}) or use other options such as http.Ok ...
	// return Response(404, nil),nil

	return Response(http.StatusNotImplemented, nil), errors.New("GetOrderById method not implemented")
}

// PlaceOrder - Place an order for a pet
func (s *StoreAPIService) PlaceOrder(ctx context.Context, Order) (ImplResponse, error) {
	// TODO - update PlaceOrder with the required logic for this service method.
	// Add api_store_service.go to the .openapi-generator-ignore to avoid overwriting this service implementation when updating open api generation.

	// TODO: Uncomment the next line to return response Response(200, Order{}) or use other options such as http.Ok ...
	// return Response(200, Order{}), nil

	// TODO: Uncomment the next line to return response Response(400, {}) or use other options such as http.Ok ...
	// return Response(400, nil),nil

	return Response(http.StatusNotImplemented, nil), errors.New("PlaceOrder method not implemented")
}
