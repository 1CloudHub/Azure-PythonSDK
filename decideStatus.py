def decide_status(self):
    # print(self)
    if (self['MetricType'] == 'CPUUtilization' and self['Maximum'] != None):
        # range should be less than 5% and max should be less than 30%
        if (self['Maximum'] - self['Minimum'] < 5 and self['Maximum'] < 30):
            return('idle')
        else:
            return('active')
    elif (self['MetricType'] == 'NetworkIn' and self['Average'] != None):
        # range should be less than 250,000 and max should be less than 500,000
        if (self['Maximum'] - self['Minimum'] < 250000 and self['Maximum'] < 500000):
            return ('idle')
        else:
            return('active')
    elif (self['MetricType'] == 'NetworkOut' and self['Average'] != None):
        # range should be less than 600,000 and max should be less than 800,000
        if (self['Maximum'] - self['Minimum'] < 600000 and self['Maximum'] < 800000):
            return ('idle')
        else:
            return('active')
    else:
        return('unavailable')