#le code source pour afficher les données du capteur qui a l'@ Mac XX:XX:XX:XX:XX:XX
import asyncio
from ruuvitag_sensor.ruuvi import RuuviTagSensor

macs = ["XX:XX:XX:XX:XX:XX"]


async def main():
    # Get data only for defineded MACs. 
    datas = []
    async for found_data in RuuviTagSensor.get_data_async(macs):
        print(f"MAC: {found_data[0]}")
        print(f"Data: {found_data[1]}")
        datas.append(found_data)
        # just a condition to exit after 10 found results
        if len(datas) > 10:
            break


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())

