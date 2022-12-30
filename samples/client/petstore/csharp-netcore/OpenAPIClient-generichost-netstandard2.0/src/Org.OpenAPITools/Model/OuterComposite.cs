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
    /// OuterComposite
    /// </summary>
    public partial class OuterComposite : IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="OuterComposite" /> class.
        /// </summary>
        /// <param name="myNumber">myNumber</param>
        /// <param name="myString">myString</param>
        /// <param name="myBoolean">myBoolean</param>
        [JsonConstructor]
        public OuterComposite(decimal myNumber, string myString, bool myBoolean)
        {
#pragma warning disable CS0472 // The result of the expression is always the same since a value of this type is never equal to 'null'
#pragma warning disable CS8073 // The result of the expression is always the same since a value of this type is never equal to 'null'

            if (myNumber == null)
                throw new ArgumentNullException("myNumber is a required property for OuterComposite and cannot be null.");

            if (myString == null)
                throw new ArgumentNullException("myString is a required property for OuterComposite and cannot be null.");

            if (myBoolean == null)
                throw new ArgumentNullException("myBoolean is a required property for OuterComposite and cannot be null.");

#pragma warning restore CS0472 // The result of the expression is always the same since a value of this type is never equal to 'null'
#pragma warning restore CS8073 // The result of the expression is always the same since a value of this type is never equal to 'null'

            MyNumber = myNumber;
            MyString = myString;
            MyBoolean = myBoolean;
        }

        /// <summary>
        /// Gets or Sets MyNumber
        /// </summary>
        [JsonPropertyName("my_number")]
        public decimal MyNumber { get; set; }

        /// <summary>
        /// Gets or Sets MyString
        /// </summary>
        [JsonPropertyName("my_string")]
        public string MyString { get; set; }

        /// <summary>
        /// Gets or Sets MyBoolean
        /// </summary>
        [JsonPropertyName("my_boolean")]
        public bool MyBoolean { get; set; }

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
            sb.Append("class OuterComposite {\n");
            sb.Append("  MyNumber: ").Append(MyNumber).Append("\n");
            sb.Append("  MyString: ").Append(MyString).Append("\n");
            sb.Append("  MyBoolean: ").Append(MyBoolean).Append("\n");
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
    /// A Json converter for type OuterComposite
    /// </summary>
    public class OuterCompositeJsonConverter : JsonConverter<OuterComposite>
    {
        /// <summary>
        /// A Json reader.
        /// </summary>
        /// <param name="reader"></param>
        /// <param name="typeToConvert"></param>
        /// <param name="options"></param>
        /// <returns></returns>
        /// <exception cref="JsonException"></exception>
        public override OuterComposite Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
        {
            int currentDepth = reader.CurrentDepth;

            if (reader.TokenType != JsonTokenType.StartObject && reader.TokenType != JsonTokenType.StartArray)
                throw new JsonException();

            JsonTokenType startingTokenType = reader.TokenType;

            decimal myNumber = default;
            string myString = default;
            bool myBoolean = default;

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
                        case "my_number":
                            myNumber = reader.GetInt32();
                            break;
                        case "my_string":
                            myString = reader.GetString();
                            break;
                        case "my_boolean":
                            myBoolean = reader.GetBoolean();
                            break;
                        default:
                            break;
                    }
                }
            }

            return new OuterComposite(myNumber, myString, myBoolean);
        }

        /// <summary>
        /// A Json writer
        /// </summary>
        /// <param name="writer"></param>
        /// <param name="outerComposite"></param>
        /// <param name="options"></param>
        /// <exception cref="NotImplementedException"></exception>
        public override void Write(Utf8JsonWriter writer, OuterComposite outerComposite, JsonSerializerOptions options)
        {
            writer.WriteStartObject();

            writer.WriteNumber("my_number", outerComposite.MyNumber);
            writer.WriteString("my_string", outerComposite.MyString);
            writer.WriteBoolean("my_boolean", outerComposite.MyBoolean);

            writer.WriteEndObject();
        }
    }
}
