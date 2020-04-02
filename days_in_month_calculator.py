def days_in_month(name):
    months = [(30, "January"), (28, "February"), (31, "March"), (30, "April"),
              (31, "May"), (30, "June"), (31, "July"), (31, "August"),
              (31, "September"), (31, "October"), (30, "November"), (31, "December")]
    for days, month in months:
        if name == month:
            return days
