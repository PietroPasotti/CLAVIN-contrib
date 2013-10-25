package controllers

import play.api._
import play.api.mvc._
import com.bericotech.clavin.GeoParser
import com.bericotech.clavin.GeoParserFactory
import com.bericotech.clavin.resolver.ResolvedLocation
import scala.collection.JavaConverters._
import play.api.libs.json.Json
import play.api.libs.json.JsObject
import play.api.libs.json.JsArray
import scala.collection.mutable.ListBuffer
import com.typesafe.config._

object Application extends Controller {
  
  def index() = Action { request =>
	    val conf = ConfigFactory.load()
   
	    println(conf.getString("clavin.index"))
    	var parser:GeoParser = GeoParserFactory.getDefault(conf.getString("clavin.index"))
		//var inputString:String = "I live in Boston"
    	val body: AnyContent = request.body
    	val textBody: Option[String] = body.asText
    	  
    	textBody.map { text =>   	    	 
    	// Parse location names in the text into geographic entities
		val resolvedLocations = parser.parse(text)
		
		val rl = resolvedLocations.asScala
    	
		val locs = new ListBuffer[JsObject]()
		for( r <- rl){
			var jl = Json.obj("geonameID" -> r.geoname.geonameID,
					 "name" -> r.geoname.name,
					 "locationText" -> r.location.text,
                     "countryName" -> r.geoname.getPrimaryCountryName(),
                     "population" -> r.geoname.population,
                     "admin1Code" -> r.geoname.admin1Code,
					 "locationPosition" -> r.location.position,
					 "fuzzy" -> r.fuzzy,
					 "confidence" -> r.confidence,
					 "latitude" -> r.geoname.latitude,
					 "longitude" -> r.geoname.longitude)
			locs.append(jl)
		}
				
    	val results = Json.obj(
			"version" -> "1.0.0",
			"locations" -> JsArray(locs)) 	
			Ok(Json.toJson(results))
    		
    		}.getOrElse {
    			BadRequest("Expecting text/plain request body")  
    	}
  	}
}
