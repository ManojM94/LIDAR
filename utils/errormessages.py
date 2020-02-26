class ErrorMessages:
    RangeValueError = "Input type of range parameters must be an Integer or Float"
    MaxMinConstraint = "Input Range minimum should be less than or equal to Range maximum"
    DValueError = "D value must be a positive Integer"
    scanError = "Invalid scan list. Data must be list same length scans and each scan must be a list"
    inputError = "Invalid scan elements. Elements must be Integer/Float."

    def __init__(self):
        pass
