<h1 align="center">OpenAPI Generator</h1>


<div align="center">

[![Stable releases in Maven Central](https://img.shields.io/maven-metadata/v/https/repo1.maven.org/maven2/org/openapitools/openapi-generator/maven-metadata.xml.svg)](http://search.maven.org/#search%7Cgav%7C1%7Cg%3A%22org.openapitools%22%20AND%20a%3A%22openapi-generator%22) [![Apache 2.0 License](https://img.shields.io/badge/License-Apache%202.0-orange)](./LICENSE) [![Open Collective backers](https://img.shields.io/opencollective/backers/openapi_generator?color=orange&label=OpenCollective%20Backers)](https://opencollective.com/openapi_generator) [![Join the Slack chat room](https://img.shields.io/badge/Slack-Join%20the%20chat%20room-orange)](https://join.slack.com/t/openapi-generator/shared_invite/zt-12jxxd7p2-XUeQM~4pzsU9x~eGLQqX2g) [![Follow OpenAPI Generator Twitter account to get the latest update](https://img.shields.io/twitter/follow/oas_generator.svg?style=social&label=Follow)](https://twitter.com/oas_generator) [![Contribute with Gitpod](https://img.shields.io/badge/Contribute%20with-Gitpod-908a85?logo=gitpod)](https://gitpod.io/#https://github.com/OpenAPITools/openapi-generator)

</div>

<div align="center">

[Master](https://github.com/OpenAPITools/openapi-generator/tree/master) (`6.3.0`):
[![Build Status](https://img.shields.io/travis/OpenAPITools/openapi-generator/master.svg?label=Integration%20Test)](https://travis-ci.com/OpenAPITools/openapi-generator)
[![Integration Test2](https://circleci.com/gh/OpenAPITools/openapi-generator.svg?style=shield)](https://circleci.com/gh/OpenAPITools/openapi-generator)
[![Windows Test](https://ci.appveyor.com/api/projects/status/github/openapitools/openapi-generator?branch=master&svg=true&passingText=Windows%20Test%20-%20OK&failingText=Windows%20Test%20-%20Fails)](https://ci.appveyor.com/project/WilliamCheng/openapi-generator)
[![Bitrise](https://img.shields.io/bitrise/4a2b10a819d12b67/master?label=bitrise%3A%20Swift+4,5&token=859FMDR8QHwabCzwvZK6vQ)](https://app.bitrise.io/app/4a2b10a819d12b67)
[![GitHub Workflow Status (branch)](https://img.shields.io/github/workflow/status/openapitools/openapi-generator/Check%20Supported%20Java%20Versions/master?label=Check%20Supported%20Java%20Versions&logo=github&logoColor=green)](https://github.com/OpenAPITools/openapi-generator/actions?query=workflow%3A%22Check+Supported+Java+Versions%22)

[7.0.x](https://github.com/OpenAPITools/openapi-generator/tree/7.0.x) (`7.0.x`):
[![Build Status](https://img.shields.io/travis/OpenAPITools/openapi-generator/7.0.x.svg?label=Integration%20Test)](https://travis-ci.com/OpenAPITools/openapi-generator)
[![Integration Test2](https://circleci.com/gh/OpenAPITools/openapi-generator/tree/7.0.x.svg?style=shield)](https://circleci.com/gh/OpenAPITools/openapi-generator)
[![Windows Test](https://ci.appveyor.com/api/projects/status/github/openapitools/openapi-generator?branch=7.0.x&svg=true&passingText=Windows%20Test%20-%20OK&failingText=Windows%20Test%20-%20Fails)](https://ci.appveyor.com/project/WilliamCheng/openapi-generator)
[![Bitrise](https://img.shields.io/bitrise/4a2b10a819d12b67/7.0.x?label=bitrise%3A%20Swift+4,5&token=859FMDR8QHwabCzwvZK6vQ)](https://app.bitrise.io/app/4a2b10a819d12b67)

</div>

<div align="center">

:star::star::star: If you would like to contribute, please refer to [guidelines](CONTRIBUTING.md) and a list of [open tasks](https://github.com/openapitools/openapi-generator/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22).:star::star::star:

:bangbang: To migrate from Swagger Codegen to OpenAPI Generator, please refer to the [migration guide](docs/migration-from-swagger-codegen.md) :bangbang:

:notebook_with_decorative_cover: For more information, please refer to the [Wiki page](https://github.com/openapitools/openapi-generator/wiki) and [FAQ](https://github.com/openapitools/openapi-generator/wiki/FAQ) :notebook_with_decorative_cover:

:notebook_with_decorative_cover: The eBook [A Beginner's Guide to Code Generation for REST APIs](https://gum.co/openapi_generator_ebook) is a good starting point for beginners :notebook_with_decorative_cover:

:warning: If the OpenAPI spec, templates or any input (e.g. options, environment variables) is obtained from an untrusted source or environment, please make sure you've reviewed these inputs before using OpenAPI Generator to generate the API client, server stub or documentation to avoid potential security issues (e.g. [code injection](https://en.wikipedia.org/wiki/Code_injection)). For security vulnerabilities, please contact [team@openapitools.org](mailto:team@openapitools.org). :warning:

:bangbang: Both "OpenAPI Tools" (https://OpenAPITools.org - the parent organization of OpenAPI Generator) and "OpenAPI Generator" are not affiliated with OpenAPI Initiative (OAI) :bangbang:

</div>

## Sponsors

If you find OpenAPI Generator useful for work, please consider asking your company to support this Open Source project by [becoming a sponsor](https://opencollective.com/openapi_generator). You can also individually sponsor the project by [becoming a backer](https://opencollective.com/openapi_generator).

#### Thank you to our bronze sponsors!

[![NamSor](https://openapi-generator.tech/img/companies/namsor.png)](https://www.namsor.com/?utm_source=openapi_generator&utm_medium=github_webpage&utm_campaign=sponsor)
[![LightBow](https://openapi-generator.tech/img/companies/lightbow.png)](https://www.lightbow.net/?utm_source=openapi_generator&utm_medium=github_webpage&utm_campaign=sponsor)
[<img src="https://openapi-generator.tech/img/companies/docspring.png" width="128" height="128">](https://docspring.com/?utm_source=openapi_generator&utm_medium=github_webpage&utm_campaign=sponsor)
[<img src="https://openapi-generator.tech/img/companies/datadog.png" width="128" height="128">](https://datadoghq.com/?utm_source=openapi_generator&utm_medium=github_webpage&utm_campaign=sponsor)
[<img src="https://openapi-generator.tech/img/companies/thales.jpg" width="128" height="128">](https://cpl.thalesgroup.com/?utm_source=openapi_generator&utm_medium=github_webpage&utm_campaign=sponsor)
[<img src="https://openapi-generator.tech/img/companies/apideck.jpg" width="128" height="128">](https://www.apideck.com/?utm_source=openapi_generator&utm_medium=github_webpage&utm_campaign=sponsor)
[<img src="https://openapi-generator.tech/img/companies/pexa.png" width="128" height="128">](https://www.pexa.com.au/?utm_source=openapi_generator&utm_medium=github_webpage&utm_campaign=sponsor)
[<img src="https://openapi-generator.tech/img/companies/numary.png" width="128" height="128">](https://www.numary.com/?utm_source=openapi_generator&utm_medium=github_webpage&utm_campaign=sponsor)
[<img src="https://openapi-generator.tech/img/companies/onesignal.png" width="128" height="128">](https://www.onesignal.com/?utm_source=openapi_generator&utm_medium=github_webpage&utm_campaign=sponsor)
[<img src="https://openapi-generator.tech/img/companies/virtualansoftware.png" width="128" height="128">](https://www.virtualansoftware.com/?utm_source=openapi_generator&utm_medium=github_webpage&utm_campaign=sponsor)
[<img src="https://openapi-generator.tech/img/companies/mergedev.jpeg" width="128" height="128">](https://www.merge.dev/?utm_source=openapi_generator&utm_medium=github_webpage&utm_campaign=sponsor)
[<img src="https://openapi-generator.tech/img/companies/burkert.jpg" width="128" height="128">](https://www.burkert.com/?utm_source=openapi_generator&utm_medium=github_webpage&utm_campaign=sponsor)
[<img src="https://openapi-generator.tech/img/companies/finbourne.png" width="128" height="128">](https://www.finbourne.com/?utm_source=openapi_generator&utm_medium=github_webpage&utm_campaign=sponsor)
[<img src="https://openapi-generator.tech/img/companies/bumpsh.png" width="128" height="128">](https://bump.sh/?utm_source=openapi_generator&utm_medium=github_webpage&utm_campaign=sponsor)

#### Thank you GoDaddy for sponsoring the domain names, Linode for sponsoring the VPS and Checkly for sponsoring the API monitoring

[<img src="https://openapi-generator.tech/img/companies/godaddy.png" width="150">](https://www.godaddy.com/?utm_source=openapi_generator&utm_medium=github_webpage&utm_campaign=sponsor)
[![Linode](https://www.linode.com/media/images/logos/standard/light/linode-logo_standard_light_small.png)](https://www.linode.com/?utm_source=openapi_generator&utm_medium=github_webpage&utm_campaign=sponsor)
[<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRAhEYadUyZYzGUotZiSdXkVMqqLGuohyixLl4eUpUV6pAbUULL" width="150">](https://checklyhq.com/?utm_source=openapi_generator&utm_medium=github_webpage&utm_campaign=sponsor)

This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

## Overview
This API client was generated by the [OpenAPI Generator](https://openapi-generator.tech) project.  By using the [OpenAPI-spec](https://www.openapis.org/) from a remote server, you can easily generate an API client.

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.GoClientCodegen

## Installation

Install the following dependencies:

```shell
go get github.com/stretchr/testify/assert
go get golang.org/x/oauth2
go get golang.org/x/net/context
```

Put the package under your project folder and add the following in import:

```golang
import openapi "github.com/GIT_USER_ID/GIT_REPO_ID"
```

To use a proxy, set the environment variable `HTTP_PROXY`:

```golang
os.Setenv("HTTP_PROXY", "http://proxy_name:proxy_port")
```

## Configuration of Server URL

Default configuration comes with `Servers` field that contains server objects as defined in the OpenAPI specification.

### Select Server Configuration

For using other server than the one defined on index 0 set context value `sw.ContextServerIndex` of type `int`.

```golang
ctx := context.WithValue(context.Background(), openapi.ContextServerIndex, 1)
```

### Templated Server URL

Templated server URL is formatted using default variables from configuration or from context value `sw.ContextServerVariables` of type `map[string]string`.

```golang
ctx := context.WithValue(context.Background(), openapi.ContextServerVariables, map[string]string{
	"basePath": "v2",
})
```

Note, enum values are always validated and all unused variables are silently ignored.

### URLs Configuration per Operation

Each operation can use different server URL defined using `OperationServers` map in the `Configuration`.
An operation is uniquely identified by `"{classname}Service.{nickname}"` string.
Similar rules for overriding default operation server index and variables applies by using `sw.ContextOperationServerIndices` and `sw.ContextOperationServerVariables` context maps.

```golang
ctx := context.WithValue(context.Background(), openapi.ContextOperationServerIndices, map[string]int{
	"{classname}Service.{nickname}": 2,
})
ctx = context.WithValue(context.Background(), openapi.ContextOperationServerVariables, map[string]map[string]string{
	"{classname}Service.{nickname}": {
		"port": "8443",
	},
})
```

## Documentation for API Endpoints

All URIs are relative to *http://petstore.swagger.io:80/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AnotherFakeApi* | [**Call123TestSpecialTags**](docs/AnotherFakeApi.md#call123testspecialtags) | **Patch** /another-fake/dummy | To test special tags
*DefaultApi* | [**FooGet**](docs/DefaultApi.md#fooget) | **Get** /foo | 
*FakeApi* | [**FakeHealthGet**](docs/FakeApi.md#fakehealthget) | **Get** /fake/health | Health check endpoint
*FakeApi* | [**FakeOuterBooleanSerialize**](docs/FakeApi.md#fakeouterbooleanserialize) | **Post** /fake/outer/boolean | 
*FakeApi* | [**FakeOuterCompositeSerialize**](docs/FakeApi.md#fakeoutercompositeserialize) | **Post** /fake/outer/composite | 
*FakeApi* | [**FakeOuterNumberSerialize**](docs/FakeApi.md#fakeouternumberserialize) | **Post** /fake/outer/number | 
*FakeApi* | [**FakeOuterStringSerialize**](docs/FakeApi.md#fakeouterstringserialize) | **Post** /fake/outer/string | 
*FakeApi* | [**TestBodyWithFileSchema**](docs/FakeApi.md#testbodywithfileschema) | **Put** /fake/body-with-file-schema | 
*FakeApi* | [**TestBodyWithQueryParams**](docs/FakeApi.md#testbodywithqueryparams) | **Put** /fake/body-with-query-params | 
*FakeApi* | [**TestClientModel**](docs/FakeApi.md#testclientmodel) | **Patch** /fake | To test \&quot;client\&quot; model
*FakeApi* | [**TestEndpointParameters**](docs/FakeApi.md#testendpointparameters) | **Post** /fake | Fake endpoint for testing various parameters 假端點 偽のエンドポイント 가짜 엔드 포인트 
*FakeApi* | [**TestEnumParameters**](docs/FakeApi.md#testenumparameters) | **Get** /fake | To test enum parameters
*FakeApi* | [**TestGroupParameters**](docs/FakeApi.md#testgroupparameters) | **Delete** /fake | Fake endpoint to test group parameters (optional)
*FakeApi* | [**TestInlineAdditionalProperties**](docs/FakeApi.md#testinlineadditionalproperties) | **Post** /fake/inline-additionalProperties | test inline additionalProperties
*FakeApi* | [**TestJsonFormData**](docs/FakeApi.md#testjsonformdata) | **Get** /fake/jsonFormData | test json serialization of form data
*FakeApi* | [**TestQueryParameterCollectionFormat**](docs/FakeApi.md#testqueryparametercollectionformat) | **Put** /fake/test-query-parameters | 
*FakeApi* | [**TestUniqueItemsHeaderAndQueryParameterCollectionFormat**](docs/FakeApi.md#testuniqueitemsheaderandqueryparametercollectionformat) | **Put** /fake/test-unique-parameters | 
*FakeClassnameTags123Api* | [**TestClassname**](docs/FakeClassnameTags123Api.md#testclassname) | **Patch** /fake_classname_test | To test class name in snake case
*PetApi* | [**AddPet**](docs/PetApi.md#addpet) | **Post** /pet | Add a new pet to the store
*PetApi* | [**DeletePet**](docs/PetApi.md#deletepet) | **Delete** /pet/{petId} | Deletes a pet
*PetApi* | [**FindPetsByStatus**](docs/PetApi.md#findpetsbystatus) | **Get** /pet/findByStatus | Finds Pets by status
*PetApi* | [**FindPetsByTags**](docs/PetApi.md#findpetsbytags) | **Get** /pet/findByTags | Finds Pets by tags
*PetApi* | [**GetPetById**](docs/PetApi.md#getpetbyid) | **Get** /pet/{petId} | Find pet by ID
*PetApi* | [**UpdatePet**](docs/PetApi.md#updatepet) | **Put** /pet | Update an existing pet
*PetApi* | [**UpdatePetWithForm**](docs/PetApi.md#updatepetwithform) | **Post** /pet/{petId} | Updates a pet in the store with form data
*PetApi* | [**UploadFile**](docs/PetApi.md#uploadfile) | **Post** /pet/{petId}/uploadImage | uploads an image
*PetApi* | [**UploadFileWithRequiredFile**](docs/PetApi.md#uploadfilewithrequiredfile) | **Post** /fake/{petId}/uploadImageWithRequiredFile | uploads an image (required)
*StoreApi* | [**DeleteOrder**](docs/StoreApi.md#deleteorder) | **Delete** /store/order/{order_id} | Delete purchase order by ID
*StoreApi* | [**GetInventory**](docs/StoreApi.md#getinventory) | **Get** /store/inventory | Returns pet inventories by status
*StoreApi* | [**GetOrderById**](docs/StoreApi.md#getorderbyid) | **Get** /store/order/{order_id} | Find purchase order by ID
*StoreApi* | [**PlaceOrder**](docs/StoreApi.md#placeorder) | **Post** /store/order | Place an order for a pet
*UserApi* | [**CreateUser**](docs/UserApi.md#createuser) | **Post** /user | Create user
*UserApi* | [**CreateUsersWithArrayInput**](docs/UserApi.md#createuserswitharrayinput) | **Post** /user/createWithArray | Creates list of users with given input array
*UserApi* | [**CreateUsersWithListInput**](docs/UserApi.md#createuserswithlistinput) | **Post** /user/createWithList | Creates list of users with given input array
*UserApi* | [**DeleteUser**](docs/UserApi.md#deleteuser) | **Delete** /user/{username} | Delete user
*UserApi* | [**GetUserByName**](docs/UserApi.md#getuserbyname) | **Get** /user/{username} | Get user by user name
*UserApi* | [**LoginUser**](docs/UserApi.md#loginuser) | **Get** /user/login | Logs user into the system
*UserApi* | [**LogoutUser**](docs/UserApi.md#logoutuser) | **Get** /user/logout | Logs out current logged in user session
*UserApi* | [**UpdateUser**](docs/UserApi.md#updateuser) | **Put** /user/{username} | Updated user


## Documentation For Models

 - [AdditionalPropertiesClass](docs/AdditionalPropertiesClass.md)
 - [Animal](docs/Animal.md)
 - [ApiResponse](docs/ApiResponse.md)
 - [Apple](docs/Apple.md)
 - [AppleReq](docs/AppleReq.md)
 - [ArrayOfArrayOfNumberOnly](docs/ArrayOfArrayOfNumberOnly.md)
 - [ArrayOfNumberOnly](docs/ArrayOfNumberOnly.md)
 - [ArrayTest](docs/ArrayTest.md)
 - [Banana](docs/Banana.md)
 - [BananaReq](docs/BananaReq.md)
 - [Capitalization](docs/Capitalization.md)
 - [Cat](docs/Cat.md)
 - [CatAllOf](docs/CatAllOf.md)
 - [Category](docs/Category.md)
 - [ClassModel](docs/ClassModel.md)
 - [Client](docs/Client.md)
 - [Dog](docs/Dog.md)
 - [DogAllOf](docs/DogAllOf.md)
 - [DuplicatedPropChild](docs/DuplicatedPropChild.md)
 - [DuplicatedPropChildAllOf](docs/DuplicatedPropChildAllOf.md)
 - [DuplicatedPropParent](docs/DuplicatedPropParent.md)
 - [EnumArrays](docs/EnumArrays.md)
 - [EnumClass](docs/EnumClass.md)
 - [EnumTest](docs/EnumTest.md)
 - [File](docs/File.md)
 - [FileSchemaTestClass](docs/FileSchemaTestClass.md)
 - [Foo](docs/Foo.md)
 - [FooGetDefaultResponse](docs/FooGetDefaultResponse.md)
 - [FormatTest](docs/FormatTest.md)
 - [Fruit](docs/Fruit.md)
 - [FruitReq](docs/FruitReq.md)
 - [GmFruit](docs/GmFruit.md)
 - [HasOnlyReadOnly](docs/HasOnlyReadOnly.md)
 - [HealthCheckResult](docs/HealthCheckResult.md)
 - [List](docs/List.md)
 - [Mammal](docs/Mammal.md)
 - [MapOfFileTest](docs/MapOfFileTest.md)
 - [MapTest](docs/MapTest.md)
 - [MixedPropertiesAndAdditionalPropertiesClass](docs/MixedPropertiesAndAdditionalPropertiesClass.md)
 - [Model200Response](docs/Model200Response.md)
 - [Name](docs/Name.md)
 - [NullableAllOf](docs/NullableAllOf.md)
 - [NullableAllOfChild](docs/NullableAllOfChild.md)
 - [NullableClass](docs/NullableClass.md)
 - [NumberOnly](docs/NumberOnly.md)
 - [OneOfPrimitiveType](docs/OneOfPrimitiveType.md)
 - [OneOfPrimitiveTypeChild](docs/OneOfPrimitiveTypeChild.md)
 - [OneOfPrimitiveTypes](docs/OneOfPrimitiveTypes.md)
 - [OneOfWithNestedPrimitiveTime](docs/OneOfWithNestedPrimitiveTime.md)
 - [OneOfWithNestedPrimitiveTimeAvatar](docs/OneOfWithNestedPrimitiveTimeAvatar.md)
 - [Order](docs/Order.md)
 - [OuterComposite](docs/OuterComposite.md)
 - [OuterEnum](docs/OuterEnum.md)
 - [OuterEnumDefaultValue](docs/OuterEnumDefaultValue.md)
 - [OuterEnumInteger](docs/OuterEnumInteger.md)
 - [OuterEnumIntegerDefaultValue](docs/OuterEnumIntegerDefaultValue.md)
 - [Pet](docs/Pet.md)
 - [PrimitiveAndPrimitiveTime](docs/PrimitiveAndPrimitiveTime.md)
 - [ReadOnlyFirst](docs/ReadOnlyFirst.md)
 - [ReadOnlyWithDefault](docs/ReadOnlyWithDefault.md)
 - [Return](docs/Return.md)
 - [SpecialModelName](docs/SpecialModelName.md)
 - [Tag](docs/Tag.md)
 - [User](docs/User.md)
 - [Whale](docs/Whale.md)
 - [Zebra](docs/Zebra.md)


## Documentation For Authorization



### api_key

- **Type**: API key
- **API key parameter name**: api_key
- **Location**: HTTP header

Note, each API key must be added to a map of `map[string]APIKey` where the key is: api_key and passed in as the auth context for each request.


### api_key_query

- **Type**: API key
- **API key parameter name**: api_key_query
- **Location**: URL query string

Note, each API key must be added to a map of `map[string]APIKey` where the key is: api_key_query and passed in as the auth context for each request.


### bearer_test

- **Type**: HTTP Bearer token authentication

Example

```golang
auth := context.WithValue(context.Background(), sw.ContextAccessToken, "BEARER_TOKEN_STRING")
r, err := client.Service.Operation(auth, args)
```


### http_basic_test

- **Type**: HTTP basic authentication

Example

```golang
auth := context.WithValue(context.Background(), sw.ContextBasicAuth, sw.BasicAuth{
    UserName: "username",
    Password: "password",
})
r, err := client.Service.Operation(auth, args)
```


### http_signature_test

- **Type**: HTTP signature authentication

Example

```golang
	authConfig := client.HttpSignatureAuth{
		KeyId:                "my-key-id",
		PrivateKeyPath:       "rsa.pem",
		Passphrase:           "my-passphrase",
		SigningScheme:        sw.HttpSigningSchemeHs2019,
		SignedHeaders:        []string{
			sw.HttpSignatureParameterRequestTarget, // The special (request-target) parameter expresses the HTTP request target.
			sw.HttpSignatureParameterCreated,       // Time when request was signed, formatted as a Unix timestamp integer value.
			"Host",                                 // The Host request header specifies the domain name of the server, and optionally the TCP port number.
			"Date",                                 // The date and time at which the message was originated.
			"Content-Type",                         // The Media type of the body of the request.
			"Digest",                               // A cryptographic digest of the request body.
		},
		SigningAlgorithm:     sw.HttpSigningAlgorithmRsaPSS,
		SignatureMaxValidity: 5 * time.Minute,
	}
	var authCtx context.Context
	var err error
	if authCtx, err = authConfig.ContextWithValue(context.Background()); err != nil {
		// Process error
	}
	r, err = client.Service.Operation(auth, args)

```

### petstore_auth


- **Type**: OAuth
- **Flow**: implicit
- **Authorization URL**: http://petstore.swagger.io/api/oauth/dialog
- **Scopes**: 
 - **write:pets**: modify pets in your account
 - **read:pets**: read your pets

Example

```golang
auth := context.WithValue(context.Background(), sw.ContextAccessToken, "ACCESSTOKENSTRING")
r, err := client.Service.Operation(auth, args)
```

Or via OAuth2 module to automatically refresh tokens and perform user authentication.

```golang
import "golang.org/x/oauth2"

/* Perform OAuth2 round trip request and obtain a token */

tokenSource := oauth2cfg.TokenSource(createContext(httpClient), &token)
auth := context.WithValue(oauth2.NoContext, sw.ContextOAuth2, tokenSource)
r, err := client.Service.Operation(auth, args)
```


## Documentation for Utility Methods

Due to the fact that model structure members are all pointers, this package contains
a number of utility functions to easily obtain pointers to values of basic types.
Each of these functions takes a value of the given basic type and returns a pointer to it:

* `PtrBool`
* `PtrInt`
* `PtrInt32`
* `PtrInt64`
* `PtrFloat`
* `PtrFloat32`
* `PtrFloat64`
* `PtrString`
* `PtrTime`

## Author



