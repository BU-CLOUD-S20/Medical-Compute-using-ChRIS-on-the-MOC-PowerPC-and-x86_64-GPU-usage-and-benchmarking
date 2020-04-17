## pfurl commands

Creating an moc-ppc64le service on pfcon:

            pfurl --verb POST --raw \
              --http  10.0.0.244:5005/api/v1/cmd \
              --httpResponseBodyParse \
              --jsonwrapper 'payload' \
              --msg \
        '{  "action": "internalctl",
            "meta": {
                        "var":     "/service/moc-ppc64le",
                        "set":     {
                            "compute": {
                                "addr": "pman-ppc64le-benchmarking-chris-on-the-moc.p9-apps.osh.massopen.cloud/pman/",
                                "baseURLpath": "api/v1/cmd/",
                                "status": "undefined",
                                "authToken": "password"
                            },
                            "data": {
                                "addr": "pfioh-ppc64le-benchmarking-chris-on-the-moc.p9-apps.osh.massopen.cloud/pfioh/",
                                "baseURLpath": "api/v1/cmd/",
                                "status": "undefined",
                                "authToken": "password"
                            }
                        }
                    }
        }'

Saying hello to the new pfcon moc-ppc64le service:

              pfurl --verb POST \
                    --raw \
                    --http 10.0.0.244:5005/api/v1/cmd \
                    --httpResponseBodyParse \
                    --jsonwrapper 'payload' \
                    --msg \
               '{  "action": "hello",
                       "meta": {
                               "askAbout":     "sysinfo",
                               "echoBack":     "Hi there!",
                               "service":      "moc-ppc64le"
                       }
               }' --quiet 
               
               
 Saying hello to pman on MOC Power9 Cluster:                
               
             pfurl --verb POST --raw --http pman-ppc64le-benchmarking-chris-on-the-moc.p9-apps.osh.massopen.cloud/pman/api/v1/cmd \
                  --jsonwrapper 'payload' --msg \
             '{  "action": "hello",
                     "meta": {
                             "askAbout":     "sysinfo",
                             "echoBack":     "Hi there!"
                     }
             }' --quiet --authToken 'password'
             
 
 Saying hello to pfioh on MOC Power9 Cluster: 
 
             pfurl --verb POST --raw --http pfioh-ppc64le-benchmarking-chris-on-the-moc.p9-apps.osh.massopen.cloud/pfioh/api/v1/cmd       --jsonwrapper 'payload' --msg  '{  "action": "hello",
             "meta": {
                             "askAbout":     "sysinfo",
                             "echoBack":     "Hi there!"
                     }
             }' --quiet   --authToken 'password'
