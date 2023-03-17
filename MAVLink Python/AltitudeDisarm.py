import asyncio
from mavsdk import System

async def run():
    # Connect to the Pixhawk 4 autopilot
    # The code assumes that the Pixhawk is connected to the computer via USB and that the device name is "/dev/ttyACM0".
    drone = System()
    await drone.connect(system_address="serial:///dev/ttyACM0:57600")

    # Set mode to stabilized
    await drone.action.set_mode("STABILIZED")

    # Arm the vehicle
    await drone.action.arm()

    # Set target altitude
    target_altitude = 10 # meters

    while True:
        # Request altitude information from the Pixhawk
        print("Requesting altitude")
        async for altitude in drone.telemetry.altitude():
            # Check if altitude is above target
            if altitude.relative_altitude_m > target_altitude:
                # Disarm the vehicle
                await drone.action.disarm()
                return

        # Sleep for 1 second before checking again
        await asyncio.sleep(1)

    # Close the connection to the Pixhawk
    await drone.disconnect()

# Run the async function
asyncio.run(run())
