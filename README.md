# Hey there
This is a quick script I made to fetch the weather from [openweathermap API](https://openweathermap.org/api).

I made this to work with my polybar setup, here's a preview of how it looks.

![preview](./images/preview.png)
## Using this
To use this, you'll first need to generate your own API key from [openweathermap website](https://openweathermap.org/api).
After you generate one, it should look something like this `XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`, a mix of characters and numbers.

After that, you'll need to change some stuff in the code, as follows.
```python
# The API key that you generated from openmapweather website.
apiKey="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# The city you want to get the weather for.
# I've used my own as an example.
city="manchester"
# The language you want to get the weather in.
# This should be an iso code of the language.
language="en"
# The measurement unit you want to get the weather in.
# This can metric for °C (celsius).
# imperial for °F (fahrenheit).
# and standard for K (kelvin). 
unit="metric"
```
That's it, the program it self will print the weather which you can then use for your polybar module.
