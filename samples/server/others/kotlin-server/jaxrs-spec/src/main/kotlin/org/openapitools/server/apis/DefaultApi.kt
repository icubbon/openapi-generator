package org.openapitools.server.apis;


import javax.ws.rs.*
import javax.ws.rs.core.Response


import java.io.InputStream



@Path("/")
@javax.annotation.Generated(value = arrayOf("org.openapitools.codegen.languages.KotlinServerCodegen"))
class DefaultApi {

    @GET
    suspend fun findPetsByStatus(@PathParam("") pathDefault: kotlin.String,@PathParam("") pathNullable: kotlin.String,@QueryParam("") @DefaultValue("available")   queryDefault: kotlin.String,@HeaderParam("header_default")  @DefaultValue("available")  headerDefault: kotlin.String,@CookieParam("") @DefaultValue("available")  cookieDefault: kotlin.String,@QueryParam("")   queryNullable: kotlin.String?,@HeaderParam("header_nullable")   headerNullable: kotlin.String?,@CookieParam("")  cookieNullable: kotlin.String?,@QueryParam("")   dollarQueryDollarDollarSign: kotlin.String?): Response {
        return Response.ok().entity("magic!").build();
    }
}
