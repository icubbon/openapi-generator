package org.openapitools.server

import .http.scaladsl.Http
import .http.scaladsl.server.Route
import org.openapitools.server.api.PetApi
import org.openapitools.server.api.StoreApi
import org.openapitools.server.api.UserApi

import .http.scaladsl.server.Directives._
import .actor.ActorSystem
import .stream.ActorMaterializer

class Controller(pet: PetApi, store: StoreApi, user: UserApi)(implicit system: ActorSystem, materializer: ActorMaterializer) {

    lazy val routes: Route = pet.route ~ store.route ~ user.route 

    Http().bindAndHandle(routes, "0.0.0.0", 9000)
}