# sudo apt install can-utils
 # sudo modprobe vcan 
# sudo ip link add dev vcan0 type vcan
 # sudo ip link set up vcan0 

# candump vcan0 Terminal (1) Receiver
 # cansend vcan0 123#1122334455667788 Terminal (2) Sender


while true; do
  cansend vcan0 123#1122334455667788
  cansend vcan0 456#414570a4
  sleep 1
done

source venv/bin/activate


#Databrocker Installing

python can_listener.py
python can_processor.py
python kuksaval_publisher.py


cansend vcan0 009#01020304
cansend vcan0 065#12345678

cansend vcan0 123#1122334455667788 (Not in the filter)

##Listening on 0.0.0.0:55555 means that 
Vehicle Signal Server (VSS) Databroker is ready to receive data on port 55555

sudo docker run -it -p 55555:55555 ghcr.io/eclipse-kuksa/kuksa-databroker:main


Docker container
   └── KUKSA Databroker server
         └── port 55555 as local host


##ERROR DEBUG :
vehicle_speed, target_speed, etc.)
 do not exist in the VSS tree, so the broker returns 404.

must map  CAN signals to valid VSS paths.

Example mapping:

CAN signal	    VSS path
vehicle_speed	Vehicle.Speed
SOC	        Vehicle.Powertrain.Battery.StateOfCharge
current 	Vehicle.Powertrain.TractionBattery.Current
