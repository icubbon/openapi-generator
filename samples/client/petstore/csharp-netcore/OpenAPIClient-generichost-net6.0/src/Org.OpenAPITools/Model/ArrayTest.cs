// <auto-generated>
/*
 * OpenAPI Petstore
 *
 * This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\
 *
 * The version of the OpenAPI document: 1.0.0
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */

using System;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Text.Json;
using System.Text.Json.Serialization;
using System.ComponentModel.DataAnnotations;
using OpenAPIClientUtils = Org.OpenAPITools.Client.ClientUtils;

namespace Org.OpenAPITools.Model
{
    /// <summary>
    /// ArrayTest
    /// </summary>
    public partial class ArrayTest : IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="ArrayTest" /> class.
        /// </summary>
        /// <param name="arrayOfString">arrayOfString</param>
        /// <param name="arrayArrayOfInteger">arrayArrayOfInteger</param>
        /// <param name="arrayArrayOfModel">arrayArrayOfModel</param>
        [JsonConstructor]
        public ArrayTest(List<string> arrayOfString, List<List<long>> arrayArrayOfInteger, List<List<ReadOnlyFirst>> arrayArrayOfModel)
        {
#pragma warning disable CS0472 // The result of the expression is always the same since a value of this type is never equal to 'null'
#pragma warning disable CS8073 // The result of the expression is always the same since a value of this type is never equal to 'null'

            if (arrayOfString == null)
                throw new ArgumentNullException("arrayOfString is a required property for ArrayTest and cannot be null.");

            if (arrayArrayOfInteger == null)
                throw new ArgumentNullException("arrayArrayOfInteger is a required property for ArrayTest and cannot be null.");

            if (arrayArrayOfModel == null)
                throw new ArgumentNullException("arrayArrayOfModel is a required property for ArrayTest and cannot be null.");

#pragma warning restore CS0472 // The result of the expression is always the same since a value of this type is never equal to 'null'
#pragma warning restore CS8073 // The result of the expression is always the same since a value of this type is never equal to 'null'

            ArrayOfString = arrayOfString;
            ArrayArrayOfInteger = arrayArrayOfInteger;
            ArrayArrayOfModel = arrayArrayOfModel;
        }

        /// <summary>
        /// Gets or Sets ArrayOfString
        /// </summary>
        [JsonPropertyName("array_of_string")]
        public List<string> ArrayOfString { get; set; }

        /// <summary>
        /// Gets or Sets ArrayArrayOfInteger
        /// </summary>
        [JsonPropertyName("array_array_of_integer")]
        public List<List<long>> ArrayArrayOfInteger { get; set; }

        /// <summary>
        /// Gets or Sets ArrayArrayOfModel
        /// </summary>
        [JsonPropertyName("array_array_of_model")]
        public List<List<ReadOnlyFirst>> ArrayArrayOfModel { get; set; }

        /// <summary>
        /// Gets or Sets additional properties
        /// </summary>
        [JsonExtensionData]
        public Dictionary<string, JsonElement> AdditionalProperties { get; } = new Dictionary<string, JsonElement>();

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class ArrayTest {\n");
            sb.Append("  ArrayOfString: ").Append(ArrayOfString).Append("\n");
            sb.Append("  ArrayArrayOfInteger: ").Append(ArrayArrayOfInteger).Append("\n");
            sb.Append("  ArrayArrayOfModel: ").Append(ArrayArrayOfModel).Append("\n");
            sb.Append("  AdditionalProperties: ").Append(AdditionalProperties).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        public IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }

    /// <summary>
    /// A Json converter for type ArrayTest
    /// </summary>
    public class ArrayTestJsonConverter : JsonConverter<ArrayTest>
    {
        /// <summary>
        /// A Json reader.
        /// </summary>
        /// <param name="reader"></param>
        /// <param name="typeToConvert"></param>
        /// <param name="options"></param>
        /// <returns></returns>
        /// <exception cref="JsonException"></exception>
        public override ArrayTest Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
        {
            int currentDepth = reader.CurrentDepth;

            if (reader.TokenType != JsonTokenType.StartObject && reader.TokenType != JsonTokenType.StartArray)
                throw new JsonException();

            JsonTokenType startingTokenType = reader.TokenType;

            List<string> arrayOfString = default;
            List<List<long>> arrayArrayOfInteger = default;
            List<List<ReadOnlyFirst>> arrayArrayOfModel = default;

            while (reader.Read())
            {
                if (startingTokenType == JsonTokenType.StartObject && reader.TokenType == JsonTokenType.EndObject && currentDepth == reader.CurrentDepth)
                    break;

                if (startingTokenType == JsonTokenType.StartArray && reader.TokenType == JsonTokenType.EndArray && currentDepth == reader.CurrentDepth)
                    break;

                if (reader.TokenType == JsonTokenType.PropertyName && currentDepth == reader.CurrentDepth - 1)
                {
                    string propertyName = reader.GetString();
                    reader.Read();

                    switch (propertyName)
                    {
                        case "array_of_string":
                            arrayOfString = JsonSerializer.Deserialize<List<string>>(ref reader, options);
                            break;
                        case "array_array_of_integer":
                            arrayArrayOfInteger = JsonSerializer.Deserialize<List<List<long>>>(ref reader, options);
                            break;
                        case "array_array_of_model":
                            arrayArrayOfModel = JsonSerializer.Deserialize<List<List<ReadOnlyFirst>>>(ref reader, options);
                            break;
                        default:
                            break;
                    }
                }
            }

            return new ArrayTest(arrayOfString, arrayArrayOfInteger, arrayArrayOfModel);
        }

        /// <summary>
        /// A Json writer
        /// </summary>
        /// <param name="writer"></param>
        /// <param name="arrayTest"></param>
        /// <param name="options"></param>
        /// <exception cref="NotImplementedException"></exception>
        public override void Write(Utf8JsonWriter writer, ArrayTest arrayTest, JsonSerializerOptions options)
        {
            writer.WriteStartObject();

            writer.WritePropertyName("array_of_string");
            JsonSerializer.Serialize(writer, arrayTest.ArrayOfString, options);
            writer.WritePropertyName("array_array_of_integer");
            JsonSerializer.Serialize(writer, arrayTest.ArrayArrayOfInteger, options);
            writer.WritePropertyName("array_array_of_model");
            JsonSerializer.Serialize(writer, arrayTest.ArrayArrayOfModel, options);

            writer.WriteEndObject();
        }
    }
}
