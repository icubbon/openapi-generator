#' Create a new DummyModel
#'
#' @description
#' to test the model name mapping
#'
#' @docType class
#' @title DummyModel
#' @description DummyModel Class
#' @format An \code{R6Class} generator object
#' @field property  character [optional]
#' @importFrom R6 R6Class
#' @importFrom jsonlite fromJSON toJSON
#' @export
DummyModel <- R6::R6Class(
  "DummyModel",
  public = list(
    `property` = NULL,
    #' Initialize a new DummyModel class.
    #'
    #' @description
    #' Initialize a new DummyModel class.
    #'
    #' @param property property
    #' @param ... Other optional arguments.
    #' @export
    initialize = function(`property` = NULL, ...) {
      if (!is.null(`property`)) {
        if (!(is.character(`property`) && length(`property`) == 1)) {
          stop(paste("Error! Invalid data for `property`. Must be a string:", `property`))
        }
        self$`property` <- `property`
      }
    },
    #' To JSON string
    #'
    #' @description
    #' To JSON String
    #'
    #' @return DummyModel in JSON format
    #' @export
    toJSON = function() {
      DummyModelObject <- list()
      if (!is.null(self$`property`)) {
        DummyModelObject[["property"]] <-
          self$`property`
      }
      DummyModelObject
    },
    #' Deserialize JSON string into an instance of DummyModel
    #'
    #' @description
    #' Deserialize JSON string into an instance of DummyModel
    #'
    #' @param input_json the JSON input
    #' @return the instance of DummyModel
    #' @export
    fromJSON = function(input_json) {
      this_object <- jsonlite::fromJSON(input_json)
      if (!is.null(this_object$`property`)) {
        self$`property` <- this_object$`property`
      }
      self
    },
    #' To JSON string
    #'
    #' @description
    #' To JSON String
    #'
    #' @return DummyModel in JSON format
    #' @export
    toJSONString = function() {
      jsoncontent <- c(
        if (!is.null(self$`property`)) {
          sprintf(
          '"property":
            "%s"
                    ',
          self$`property`
          )
        }
      )
      jsoncontent <- paste(jsoncontent, collapse = ",")
      json_string <- as.character(jsonlite::minify(paste("{", jsoncontent, "}", sep = "")))
    },
    #' Deserialize JSON string into an instance of DummyModel
    #'
    #' @description
    #' Deserialize JSON string into an instance of DummyModel
    #'
    #' @param input_json the JSON input
    #' @return the instance of DummyModel
    #' @export
    fromJSONString = function(input_json) {
      this_object <- jsonlite::fromJSON(input_json)
      self$`property` <- this_object$`property`
      self
    },
    #' Validate JSON input with respect to DummyModel
    #'
    #' @description
    #' Validate JSON input with respect to DummyModel and throw an exception if invalid
    #'
    #' @param input the JSON input
    #' @export
    validateJSON = function(input) {
      input_json <- jsonlite::fromJSON(input)
    },
    #' To string (JSON format)
    #'
    #' @description
    #' To string (JSON format)
    #'
    #' @return String representation of DummyModel
    #' @export
    toString = function() {
      self$toJSONString()
    },
    #' Return true if the values in all fields are valid.
    #'
    #' @description
    #' Return true if the values in all fields are valid.
    #'
    #' @return true if the values in all fields are valid.
    #' @export
    isValid = function() {
      TRUE
    },
    #' Return a list of invalid fields (if any).
    #'
    #' @description
    #' Return a list of invalid fields (if any).
    #'
    #' @return A list of invalid fields (if any).
    #' @export
    getInvalidFields = function() {
      invalid_fields <- list()
      invalid_fields
    },
    #' Print the object
    #'
    #' @description
    #' Print the object
    #'
    #' @export
    print = function() {
      print(jsonlite::prettify(self$toJSONString()))
      invisible(self)
    }
  ),
  # Lock the class to prevent modifications to the method or field
  lock_class = TRUE
)
## Uncomment below to unlock the class to allow modifications of the method or field
# DummyModel$unlock()
#
## Below is an example to define the print function
# DummyModel$set("public", "print", function(...) {
#   print(jsonlite::prettify(self$toJSONString()))
#   invisible(self)
# })
## Uncomment below to lock the class to prevent modifications to the method or field
# DummyModel$lock()

