import asyncio


# used when cpu is idle during network calls / db results
# co-routines are wrapped functions but running async-ly
# async returns a co-routine object and is exec by await
def foo():
    return "inside await"


async def main():
    # await foo()
    print("in async")


asyncio.run(main())
# events loop -> run else we will get "RuntimeWarning: coroutine 'main' was never awaited"
# asyncio.run()
# asyncio.sleep()
# asyncio.create_task()

# main()