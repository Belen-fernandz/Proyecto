/* Magic Mirror Config Sample
 *
 * By Michael Teeuw https://michaelteeuw.nl
 * MIT Licensed.
 *
 * For more information on how you can configure this file
 * See https://github.com/MichMich/MagicMirror#configuration
 *
 */
var config = {
	address: "0.0.0.0", 	// Address to listen on, can be:
							// - "localhost", "127.0.0.1", "::1" to listen on loopback interface
							// - another specific IPv4/6 to listen on a specific interface
							// - "0.0.0.0", "::" to listen on any interface
							// Default, when address config is left out or empty, is "localhost"
	port: 8080,
	basePath: "/", 	// The URL path where MagicMirror is hosted. If you are using a Reverse proxy
					// you must set the sub path here. basePath must end with a /
	ipWhitelist: ["127.0.0.1", "::ffff:127.0.0.1", "::1", "::ffff:192.168.0.1/120", "192.168.0.1/24"], 	// Set [] to allow all IP addresses
															// or add a specific IPv4 of 192.168.1.5 :
															// ["127.0.0.1", "::ffff:127.0.0.1", "::1", "::ffff:192.168.1.5"],
															// or IPv4 range of 192.168.3.0 --> 192.168.3.15 use CIDR format :
															// ["127.0.0.1", "::ffff:127.0.0.1", "::1", "::ffff:192.168.3.0/28"],

	useHttps: false, 		// Support HTTPS or not, default "false" will use HTTP
	httpsPrivateKey: "", 	// HTTPS private key path, only require when useHttps is true
	httpsCertificate: "", 	// HTTPS Certificate path, only require when useHttps is true

	language: "es",
	logLevel: ["INFO", "LOG", "WARN", "ERROR"],
	timeFormat: 24,
	units: "metric",
	// serverOnly:  true/false/"local" ,
	// local for armv6l processors, default
	//   starts serveronly and then starts chrome browser
	// false, default for all NON-armv6l devices
	// true, force serveronly mode, because you want to.. no UI on this device

	modules: [
		    {
			        module: "alert",
		    },
		    {   
			        module: "updatenotification",
			        position: "top_bar"
		    },
		    { #Reloj
			        module: "clock",
			        position: "top_left"
		    },
		    { #HolaMundo
                    module: "helloworld",
                    position: "bottom_bar",
                    config: {
                            text: "HOLA BELÉN"
                        }
            },
            { #Calendario
                    module: "calendar",
                    header: "Proximos Eventos",
                    position: "top_left",
                    config: {
                            colored: false,
                            coloredSymbolOnly: false,
                            calendars: [
                            {
                                url:"https://calendar.google.com/calendar/ical/yuliana.belen.fernandez%40gmail.com/private-6ab65e0ba1fd8c57587c7c46ce802529/basic.ics",

                                symbol: "calendar",
                                auth: {
                                        user: "yuliana.belen.fernandez@gmail.com",
                                        pass: "1demarzo",
                                        method: "basic"
                                }
                            },
                        ],
                    },
            },
            { #Cumplidos
                    module: "compliments",
                    position: "lower_third",
                    config: {
                            compliments: {
                                    anytime: [
                                            "¡Si Puedes Soñarlo, Puedes Hacerlo!"
                                    ],
                                    morning: [
                                            "¡Buenos Dias, Hermosa!",
                                            "¡Hoy Es Un Dia Fabuloso!",
                                            "¡Vivir Solo Cuesta Vida!"
                                    ],
                                    afternoon: [
                                            "Jamas Bajes Los Brazos",
                                            "Te Ves Alucinante",
                                            "Tu Sonrisa Es Hermosa"
                                    ],
                                    evening: [
                                            "¡Eres Perfecta, Que Nadie Te Diga Lo Contrario!",
                                            "¡Sueña, Vivi, Ama, Se Libre!",
                                            "¡Nunca Pares De Soñar!"
                                    ],
                            },
                    },
            },
		    {
                    module: "currentweather",
                    position: "top_right",
                    config: {
                            location: "Buenos Aires",
                            locationID: "3435910",
                            appid: "0c3fb84b2c0820ae892fbc1f03f881cb"
                    },
            },
            {
                    module: "weatherforecast",
                    position: "top_right",
                    header: "Clima de la Semana",
                    config: {
                            location: "Buenos Aires",
                            locationID: "3435910",
                            appid: "0c3fb84b2c0820ae892fbc1f03f881cb"
                        }
            },
	        {
			        module : "MMM-Screencast",
			        position : "bottom_right",  // Esta posición es para un <div /> oculto y no para la 
			        config: {
				        position : "center",
				        height : 300,
				        ancho : 500,
			        }
        	},
		    {
   		 	        module: 'MMM-Remote-Control',
    			    position: 'bottom_left',
    			    config: {
        			        customCommand: {},  // Optional, See "Using Custom Commands" below
        			        customMenu: "custom_menu.json", // Optional, See "Custom Menu Items" below
        			        showModuleApiMenu: true, // Optional, Enable the Module Controls menu
        			        apiKey: "",         // Optional, See API/README.md for details
    			    }
		    },
		    /*{
  			    module : "MMM-GoogleAssistant",
  			    posición : "fullscreen_above",
  			    config : {
    				    debug : false,
    				    assistantConfig : {
      				        lang : "es-ES" ,
      					    projectId : "" ,  // Requerido para usar gaction.
      					    modelId : "" ,  // (OPCIONAL para gaction)
      					    instanceId : "" ,  // (OPCIONAL para gaction)
      					    latitude : 51.508530 ,
      					    longitude : -0.076132 ,
    				    } ,
    				    responseConfig : {
      					    useScreenOutput : verdad ,
      					    screenOutputCSS : "screen_output.css" ,
      					    screenOutputTimer : 5000 ,
      					    ScreenRotate : falsa ,
      					    activateDelay : 250 ,
      					    useAudioOutput : verdad ,
      					    useChime : verdad ,
      					    newChime : falsa ,
      					    useNative : falsa ,
      					    playProgram : " mpg321 "
    				    },
    				    micConfig : {  // poner allí la configuración generada por el
      					    recorder : "arecord" ,
      					    dispositivo : "plughw: 2" ,
    				    },
    				    customActionConfig : {
      					    autoMakeAction : false ,
     					    autoUpdateAction : false ,  // en RPI, la CLI de gaction podría tener algunos problemas (la versión actual debería ser 2.2.4, pero para linux-arm, Google no se ha actualizado) así que deje esto como falso en RPI. No sé si está resuelto o no. 
      					    actionLocale : "en-US" , // En este momento, no se admiten varios idiomas, lo siento. Algún día trabajaré. 
    				    },
    				    snowboy : {
      					    usePMDL : false ,
      					    audioGain : 2.0 ,
      					    Frontend : true ,
      					    Model : "alexa" ,
      					    Sensibilidad : null
                        },
    				    A2DServer : {
      					    useA2D : false ,
      					    stopCommand : "stop" ,
      					    useYouTube : true ,
      					    displayResponse : true
    			        },
				    recetas : [
   					    "con-MMM-TelegramBot.js" ,  "con-MMM-Spotify"
					],
    				NPMCheck : {
      					useChecker : true ,
      					delay : 10 * 60 * 1000 ,
      					useAlert : true
    				}
  			}
		},*/
		*/{
  			module: "MMM-GoogleAssistant",
  			position: "fullscreen_above",
  			config: {
    				assistantConfig: {
      					latitude: 51.508530,
      					longitude: -0.076132,
    				},
    				micConfig: { // put there configuration generated by auto-installer
      				recorder: "arecord",
      				device: "plughw:2",
    				},
  			}
		},*/
		{
			módulo : 'MMM-PIR-Sensor' ,
			config : {
			// Consulte 'Opciones de configuración' para obtener más información.
			}
		},
                {
                        module: "newsfeed",
                        position: "bottom_bar",
                        config: {
                                feeds: [
                                        {
                                                title: "Noticias del Dia",
                                                url: "https://tn.com.ar/rss.xml"
                                        },
                                        {
                                                title: "Noticias de Tecnologia",
                                                url: "https://www.clarin.com/rss/tecnologia/"
                                        },
                                        {
                                                title: "Noticias de Musica",
                                                url: "https://www.clarin.com/rss/eespectaculos/musica/"
                                        }
                                ],
                                showSourceTitle: true,
                                showPublishDate: true,
                                broadcastNewsFeeds: true,
                                broadcastNewsUpdates: true,
                                showDescription: true,
                                updateInterval: 7500
                        }
                },

	]
};

/*************** DO NOT EDIT THE LINE BELOW ***************/
if (typeof module !== "undefined") {module.exports = config;}
