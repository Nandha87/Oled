import lgpio

h = lgpio.gpiochip_open(0)      # Open GPIO chip
lgpio.gpio_claim_output(h, 24)  # Set GPIO24 as output
lgpio.gpio_write(h, 24, 1)      # Turn it ON
lgpio.gpio_write(h, 24, 0)      # Turn it OFF
lgpio.gpiochip_close(h)
print("GPIO test done!")
