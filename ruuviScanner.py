#Afficher les données de tous les capteurs ruuviv présents
import asyncio
from ruuvitag_sensor.ruuvi import RuuviTagSensor


async def main():
    async for found_data in RuuviTagSensor.get_data_async():
        print(f"MAC: {found_data[0]}")
        print(f"Data: {found_data[1]}")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())