"""
import asyncio
import random

async def donwload_process(file):
    print(f'Descargando archivo {file}')
    time=random.randint(1,10)
    await asyncio.sleep(time)
    print(f'{file} downloaded')
    return file

async def main():
    print('Inicio de la descarga')
    result=await donwload_process('file1.txt')
    result1=await donwload_process('file2.txt')
    result2=await donwload_process('file3.txt')
    print(f'{result,result1,result2}')


asyncio.run(main())"""

import asyncio
import random
import sys

async def download_process(file):
    print(f'Descargando archivo {file}')
    duration = random.randint(1, 10)
    bar_length = 30  # longitud visual de la barra

    for i in range(duration + 1):
        percent = i / duration
        filled = int(bar_length * percent)
        bar = '█ ' * filled + '- ' * (bar_length - filled)
        sys.stdout.write(f'\r{file} |{bar}| {int(percent*100)}%')
        sys.stdout.flush()
        await asyncio.sleep(1)

    print(f'\n{file} descargado')
    return file

async def main():
    print('Inicio de la descarga')
    result = await download_process('file1.txt')
    result1 = await download_process('file2.txt')
    result2 = await download_process('file3.txt')
    print(f'{result, result1, result2}')

asyncio.run(main())
