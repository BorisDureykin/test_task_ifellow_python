def task_4(hours, minutes):
    if hours < 0 or hours >= 24 or minutes < 0 or minutes >= 60:
        return "Недопустимое время"
    hours = hours - 12 if hours >= 12 else hours
    angle = abs(((30 * hours) + (0.5*minutes)) - (6 * minutes))
    angle = 360- angle if angle > 180 else angle

    return f"Угол между стрелками: {angle:.2f} градусов"
