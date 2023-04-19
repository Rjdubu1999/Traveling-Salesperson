

class DeliveryTruck:

    def __init__(self, carry_capacity, mph, packages, current_location, miles_traveled, day_start, current_time, day_end):
        self.carry_capacity = carry_capacity
        self.speed = mph
        self.miles_traveled = miles_traveled
        self.packages = packages
        self.current_location = current_location
        self.day_start = day_start
        self.current_time = current_time
        self.day_end = day_end

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (self.carry_capacity, self.speed, self.miles_traveled, self.packages,
                                                   self.current_location, self.day_start, self.current_time, self.day_end)


# may not need end day, mph, or capacity