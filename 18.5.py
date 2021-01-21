import redis


red = redis.Redis(
    host='redis-13960.c80.us-east-1-2.ec2.cloud.redislabs.com',
    port=13960,
    password='mSvCmI0rOjcTNqqDgRlBzauZviMjUXF3'
)

red.set('var1','value')
print(red.get('var1'))