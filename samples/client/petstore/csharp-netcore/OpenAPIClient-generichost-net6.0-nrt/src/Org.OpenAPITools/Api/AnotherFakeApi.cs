// <auto-generated>
/*
 * OpenAPI Petstore
 *
 * This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\
 *
 * The version of the OpenAPI document: 1.0.0
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */

#nullable enable

using System;
using System.Collections.Generic;
using System.Net;
using System.Threading.Tasks;
using Microsoft.Extensions.Logging;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text.Json;
using Org.OpenAPITools.Client;
using Org.OpenAPITools.Model;

namespace Org.OpenAPITools.IApi
{
    /// <summary>
    /// Represents a collection of functions to interact with the API endpoints
    /// This class is registered as transient.
    /// </summary>
    public interface IAnotherFakeApi : IApi
    {
        /// <summary>
        /// To test special tags
        /// </summary>
        /// <remarks>
        /// To test special tags and operation ID starting with number
        /// </remarks>
        /// <exception cref="ApiException">Thrown when fails to make API call</exception>
        /// <param name="modelClient">client model</param>
        /// <param name="cancellationToken">Cancellation Token to cancel the request.</param>
        /// <returns>Task&lt;ApiResponse&lt;ModelClient?&gt;&gt;</returns>
        Task<ApiResponse<ModelClient?>> Call123TestSpecialTagsWithHttpInfoAsync(ModelClient modelClient = null, System.Threading.CancellationToken? cancellationToken = null);

        /// <summary>
        /// To test special tags
        /// </summary>
        /// <remarks>
        /// To test special tags and operation ID starting with number
        /// </remarks>
        /// <exception cref="ApiException">Thrown when fails to make API call</exception>
        /// <param name="modelClient">client model</param>
        /// <param name="cancellationToken">Cancellation Token to cancel the request.</param>
        /// <returns>Task of ApiResponse&lt;ModelClient&gt;</returns>
        Task<ModelClient> Call123TestSpecialTagsAsync(ModelClient modelClient = null, System.Threading.CancellationToken? cancellationToken = null);

        /// <summary>
        /// To test special tags
        /// </summary>
        /// <remarks>
        /// To test special tags and operation ID starting with number
        /// </remarks>
        /// <param name="modelClient">client model</param>
        /// <param name="cancellationToken">Cancellation Token to cancel the request.</param>
        /// <returns>Task of ApiResponse&lt;ModelClient?&gt;</returns>
        Task<ModelClient?> Call123TestSpecialTagsOrDefaultAsync(ModelClient modelClient = null, System.Threading.CancellationToken? cancellationToken = null);
    }
}

namespace Org.OpenAPITools.Api
{
    /// <summary>
    /// Represents a collection of functions to interact with the API endpoints
    /// </summary>
    public partial class AnotherFakeApi : IApi.IAnotherFakeApi
    {
        private JsonSerializerOptions _jsonSerializerOptions;

        /// <summary>
        /// The logger
        /// </summary>
        public ILogger<AnotherFakeApi> Logger { get; }

        /// <summary>
        /// The HttpClient
        /// </summary>
        public HttpClient HttpClient { get; }

        /// <summary>
        /// A token provider of type <see cref="ApiKeyProvider"/>
        /// </summary>
        public TokenProvider<ApiKeyToken> ApiKeyProvider { get; }

        /// <summary>
        /// A token provider of type <see cref="BearerToken"/>
        /// </summary>
        public TokenProvider<BearerToken> BearerTokenProvider { get; }

        /// <summary>
        /// A token provider of type <see cref="BasicTokenProvider"/>
        /// </summary>
        public TokenProvider<BasicToken> BasicTokenProvider { get; }

        /// <summary>
        /// A token provider of type <see cref="HttpSignatureTokenProvider"/>
        /// </summary>
        public TokenProvider<HttpSignatureToken> HttpSignatureTokenProvider { get; }

        /// <summary>
        /// A token provider of type <see cref="OauthTokenProvider"/>
        /// </summary>
        public TokenProvider<OAuthToken> OauthTokenProvider { get; }

        /// <summary>
        /// Initializes a new instance of the <see cref="AnotherFakeApi"/> class.
        /// </summary>
        /// <returns></returns>
        public AnotherFakeApi(ILogger<AnotherFakeApi> logger, HttpClient httpClient, JsonSerializerOptionsProvider jsonSerializerOptionsProvider, 
            TokenProvider<ApiKeyToken> apiKeyProvider, 
            TokenProvider<BearerToken> bearerTokenProvider, 
            TokenProvider<BasicToken> basicTokenProvider, 
            TokenProvider<HttpSignatureToken> httpSignatureTokenProvider, 
            TokenProvider<OAuthToken> oauthTokenProvider)
        {
            _jsonSerializerOptions = jsonSerializerOptionsProvider.Options;
            Logger = logger;
            HttpClient = httpClient;
            ApiKeyProvider = apiKeyProvider;
            BearerTokenProvider = bearerTokenProvider;
            BasicTokenProvider = basicTokenProvider;
            HttpSignatureTokenProvider = httpSignatureTokenProvider;
            OauthTokenProvider = oauthTokenProvider;
        }

        /// <summary>
        /// Logs the api response
        /// </summary>
        /// <param name="args"></param>
        protected virtual void OnApiResponded(ApiResponseEventArgs args)
        {
            Logger.LogInformation("{0,-9} | {1} | {3}", (args.ReceivedAt - args.RequestedAt).TotalSeconds, args.HttpStatus, args.Path);
        }

        /// <summary>
        /// To test special tags To test special tags and operation ID starting with number
        /// </summary>
        /// <exception cref="ApiException">Thrown when fails to make API call</exception>
        /// <param name="modelClient">client model</param>
        /// <param name="cancellationToken">Cancellation Token to cancel the request.</param>
        /// <returns><see cref="Task"/>&lt;<see cref="ModelClient"/>&gt;</returns>
        public async Task<ModelClient> Call123TestSpecialTagsAsync(ModelClient modelClient = null, System.Threading.CancellationToken? cancellationToken = null)
        {
            ApiResponse<ModelClient?> result = await Call123TestSpecialTagsWithHttpInfoAsync(modelClient, cancellationToken).ConfigureAwait(false);

            if (result.Content == null)
                throw new ApiException(result.ReasonPhrase, result.StatusCode, result.RawContent);

            return result.Content;
        }

        /// <summary>
        /// To test special tags To test special tags and operation ID starting with number
        /// </summary>
        /// <exception cref="ApiException">Thrown when fails to make API call</exception>
        /// <param name="modelClient">client model</param>
        /// <param name="cancellationToken">Cancellation Token to cancel the request.</param>
        /// <returns><see cref="Task"/>&lt;<see cref="ModelClient"/>&gt;</returns>
        public async Task<ModelClient?> Call123TestSpecialTagsOrDefaultAsync(ModelClient modelClient = null, System.Threading.CancellationToken? cancellationToken = null)
        {
            ApiResponse<ModelClient?>? result = null;
            try 
            {
                result = await Call123TestSpecialTagsWithHttpInfoAsync(modelClient, cancellationToken).ConfigureAwait(false);
            }
            catch (Exception)
            {
            }

            return result != null && result.IsSuccessStatusCode
                ? result.Content
                : null;
        }

        /// <summary>
        /// Validates the request parameters
        /// </summary>
        /// <param name="modelClient"></param>
        /// <returns></returns>
        protected virtual ModelClient? OnCall123TestSpecialTags(ModelClient? modelClient)
        {
            return modelClient;
        }

        /// <summary>
        /// Processes the server response
        /// </summary>
        /// <param name="apiResponse"></param>
        /// <param name="modelClient"></param>
        protected virtual void AfterCall123TestSpecialTags(ApiResponse<ModelClient?> apiResponse, ModelClient? modelClient)
        {
        }

        /// <summary>
        /// Processes the server response
        /// </summary>
        /// <param name="exception"></param>
        /// <param name="pathFormat"></param>
        /// <param name="path"></param>
        /// <param name="modelClient"></param>
        protected virtual void OnErrorCall123TestSpecialTags(Exception exception, string pathFormat, string path, ModelClient? modelClient)
        {
            Logger.LogError(exception, "An error occurred while sending the request to the server.");
        }

        /// <summary>
        /// To test special tags To test special tags and operation ID starting with number
        /// </summary>
        /// <exception cref="ApiException">Thrown when fails to make API call</exception>
        /// <param name="modelClient">client model</param>
        /// <param name="cancellationToken">Cancellation Token to cancel the request.</param>
        /// <returns><see cref="Task"/>&lt;<see cref="ApiResponse{T}"/>&gt; where T : <see cref="ModelClient"/></returns>
        public async Task<ApiResponse<ModelClient?>> Call123TestSpecialTagsWithHttpInfoAsync(ModelClient modelClient = null, System.Threading.CancellationToken? cancellationToken = null)
        {
            UriBuilder uriBuilder = new UriBuilder();

            try
            {
                modelClient = OnCall123TestSpecialTags(modelClient);

                using (HttpRequestMessage request = new HttpRequestMessage())
                {
                    uriBuilder.Host = HttpClient.BaseAddress!.Host;
                    uriBuilder.Port = HttpClient.BaseAddress!.Port;
                    uriBuilder.Scheme = ClientUtils.SCHEME;
                    uriBuilder.Path = ClientUtils.CONTEXT_PATH + "/another-fake/dummy";

                    request.Content = (modelClient as object) is System.IO.Stream stream
                        ? request.Content = new StreamContent(stream)
                        : request.Content = new StringContent(JsonSerializer.Serialize(modelClient, _jsonSerializerOptions));



                    request.RequestUri = uriBuilder.Uri;

                    string[] contentTypes = new string[] {
                        "application/json" 
                    };

                    string? contentType = ClientUtils.SelectHeaderContentType(contentTypes);

                    if (contentType != null)
                        request.Content.Headers.ContentType = new MediaTypeHeaderValue(contentType);

                    string[] accepts = new string[] { 
                        "application/json" 
                    };

                    string? accept = ClientUtils.SelectHeaderAccept(accepts);

                    if (accept != null)
                        request.Headers.Accept.Add(new MediaTypeWithQualityHeaderValue(accept));

                    request.Method = HttpMethod.Patch;

                    DateTime requestedAt = DateTime.UtcNow;

                    using (HttpResponseMessage responseMessage = await HttpClient.SendAsync(request, cancellationToken.GetValueOrDefault()).ConfigureAwait(false))
                    {
                        OnApiResponded(new ApiResponseEventArgs(requestedAt, DateTime.UtcNow, responseMessage.StatusCode, "/another-fake/dummy", uriBuilder.Path));

                        string responseContent = await responseMessage.Content.ReadAsStringAsync(cancellationToken.GetValueOrDefault()).ConfigureAwait(false);

                        ApiResponse<ModelClient?> apiResponse = new ApiResponse<ModelClient?>(responseMessage, responseContent);

                        if (apiResponse.IsSuccessStatusCode)
                        {
                            apiResponse.Content = JsonSerializer.Deserialize<ModelClient>(apiResponse.RawContent, _jsonSerializerOptions);
                            AfterCall123TestSpecialTags(apiResponse, modelClient);
                        }

                        return apiResponse;
                    }
                }
            }
            catch(Exception e)
            {
                OnErrorCall123TestSpecialTags(e, "/another-fake/dummy", uriBuilder.Path, modelClient);
                throw;
            }
        }
    }
}
