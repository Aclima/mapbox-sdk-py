class ValidationError(ValueError):
    pass


class InvalidCountryCodeError(ValidationError):
    pass


class InvalidPlaceTypeError(ValidationError):
    pass


class InvalidProfileError(ValidationError):
    pass


class InvalidFeatureError(ValidationError):
    pass


class HTTPError(ValidationError):
    pass


class InvalidCoordError(ValidationError):
    pass


class InputSizeError(ValidationError):
    pass


class ImageSizeError(ValidationError):
    pass


class TokenError(ValidationError):
    pass


class InvalidParameterError(ValidationError):
    pass


class InvalidFileError(ValidationError):
    pass


class InvalidResourceTypeError(ValidationError):
    pass


class InvalidPeriodError(ValidationError):
    pass


class InvalidUsernameError(ValidationError):
    pass


class InvalidId(ValidationError):
    pass


class MapboxDeprecationWarning(UserWarning):
    pass


class InvalidZoomError(ValidationError):
    pass


class InvalidColumnError(ValidationError):
    pass


class InvalidRowError(ValidationError):
    pass


class InvalidFileFormatError(ValidationError):
    pass

class InvalidTilesetTypeError(ValidationError):
    """InvalidTilesetTypeError

    Parameters
    ----------
    message : str, optional
        A human-readable string describing the error.
    """

    pass


class InvalidVisibilityError(ValidationError):
    """InvalidVisibilityError

    Parameters
    ----------
    message : str, optional
        A human-readable string describing the error.
    """

    pass


class InvalidSortbyError(ValidationError):
    """InvalidSortbyError

    Parameters
    ----------
    message : str, optional
        A human-readable string describing the error.
    """

    pass


class InvalidLimitError(ValidationError):
    """InvalidLimitError

    Parameters
    ----------
    message : str, optional
        A human-readable string describing the error.
    """

class InvalidFeatureFormatError(ValidationError):
    pass


class InvalidMarkerNameError(ValidationError):
    pass


class InvalidLabelError(ValidationError):
    pass


class InvalidColorError(ValidationError):
    pass
