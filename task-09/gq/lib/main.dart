import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';
import 'package:flutter_osm_plugin/flutter_osm_plugin.dart';
import 'package:osm_flutter_hooks/osm_flutter_hooks.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';

ValueNotifier<double>dist = ValueNotifier(0);
ValueNotifier<double>time = ValueNotifier(0);


void main() {
  runApp(const MyApp());

}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Geo Quest',
      theme: ThemeData(
        primarySwatch: Colors.green,
      ),
      home: const MyHomePage(title: 'Geo Quest'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});
  
  final String title;
  

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  
  @override
  Widget build(BuildContext context) {
    
    return Scaffold(
      appBar: AppBar(
        centerTitle: true,
        title: Text(widget.title),
      ),
      body: const Center(
        
        child: SimpleOSM(),
      ),
      
      
    );
  }
}
class SimpleOSM extends HookWidget {
  const SimpleOSM({super.key});
  Widget isLoading(BuildContext context){
    return Scaffold(
      body: const Center(
        child:SpinKitFadingCube(
            color: Colors.green,
            size: 85,
          ),
    ));
  }
  @override
  Widget build(BuildContext context) {
    MapController Controller = MapController(
      initPosition: GeoPoint(latitude: 47.4358055, longitude: 8.4737324),
      areaLimit: BoundingBox( 
          east: 10.4922941, 
          north: 47.8084648, 
          south: 45.817995, 
          west:  5.9559113,
      ));
    
    useMapIsReady(controller: Controller, mapIsReady: () async {
        await Controller.setZoom(zoomLevel: 14);
      },);
    

    
    useMapListener(
        controller: Controller,
        
        onSingleTap: (p) async{
        GeoPoint current_pos = await Controller.myLocation();
        List<GeoPoint> geoPoints = await Controller.geopoints;

        await Controller.removeMarkers(geoPoints);
        await Controller.addMarker(p);
        await Controller.removeLastRoad();
        RoadInfo roadInfo = await Controller.drawRoad( 
          p,
          current_pos,
          roadType: RoadType.car,
          
          roadOption: RoadOption(
              roadWidth: 12,
              roadColor: Colors.blue,
              zoomInto: true,
        ),
    );
    
    dist.value = roadInfo.distance!;
    time.value = roadInfo.duration!;
    
    
  
        });
    
    return Scaffold(
      
      body :OSMFlutter( 
        controller:Controller,
        mapIsLoading: isLoading(context),
        osmOption: OSMOption(
              userTrackingOption: UserTrackingOption(
              enableTracking: true,
              unFollowUser: false,
            ),
          
            zoomOption: ZoomOption(
                  initZoom: 20,
                  minZoomLevel: 3,
                  maxZoomLevel: 19,
                  stepZoom: 1.0,
            ),
            userLocationMarker: UserLocationMaker(
                personMarker: MarkerIcon(
                    icon: Icon(
                        Icons.person_pin_circle_outlined,
                        color: Colors.red,
                        size: 100,
                    ),
                ),
            directionArrowMarker: MarkerIcon(
                    icon: Icon(
                        Icons.double_arrow,
                        size: 48,
                    ),
                ),
            ),
            roadConfiguration: RoadOption(
                    roadColor: const Color.fromARGB(255, 43, 255, 0),
            ),
            markerOption: MarkerOption(
                defaultMarker: MarkerIcon(
                    icon: Icon(
                      Icons.person_pin_circle_sharp,
                      color: Colors.black,
                      size: 35,
                    ),
                )
            ),
        )
    ),
    floatingActionButton: FloatingActionButton(onPressed: ()async{
      Controller.removeLastRoad();
      List<GeoPoint> geoPoints = await Controller.geopoints;
      Controller.removeMarkers(geoPoints);
      dist.value = 0.0;
      time.value = 0.0;
    },
    child: Icon(Icons.cancel),
    backgroundColor: Colors.green,
    foregroundColor: Colors.white,
    ),
    floatingActionButtonLocation: FloatingActionButtonLocation.centerDocked,
    bottomNavigationBar: BottomAppBar(
    
        height: 75,
        shape: CircularNotchedRectangle(),
        
        child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            ValueListenableBuilder(valueListenable: dist,
              builder: (context, name, child){
                final dis = dist.value;
                final distance = dist.value.toStringAsFixed(2);
                if(dis == 0 ){
                  return Text("     Tap to anywhere on the map to add marker !!");
                }
                else{
                  return Text("Distance :\n${distance} KM");
                }
        }),
        ValueListenableBuilder(valueListenable: dist,
          builder: (context, name, child){
            final hours = time.value/3600;
            final s = time.value%3600;
            final min = s/60;
            if(hours!=0 || min != 0){
                if (hours.round() == 0){
              return Text("Duration :\n${min.round()} min");
              }else if(hours > 0 && min == 0){
              return Text("Duration :\n${hours.round()} hr");
              }else{
              return Text("Duration :\n${hours.round()} hr ${min.round()} min");
            }
          }else{
            return Text(" ");
          }
            
            
    }),
  ],
    ),
      ),
    );
  }
}

