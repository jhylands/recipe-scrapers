import re

from functools import wraps


TIME_REGEX = re.compile(r'(\D*(?P<hours>\d+)\s*(hour|hours|hrs|hr|h|Hours|H))?(\D*(?P<minutes>\d+)\s*(minute|minutes|mins|min|m|Minutes|M))?')

      
def get_minutes_from_string(tstring):
    try:
        matched_dict = [match.groupdict() for match in TIME_REGEX.finditer(tstring) if match.groupdict().get('hours') or match.groupdict().get('minutes')]
        minutes = sum(map(int, [match.get('minutes') for match in matched_dict if match.get('minutes')]))
        minutes += 60 * sum(map(int, [match.get('hours') for match in matched_dict if match.get('hours')]))
        return minutes
    except AttributeError:  # if dom_element not found or no matched
        return 0


def get_minutes(element):
    tstring = element.get_text()
    return get_minutes_from_string(tstring)


def normalize_string(string):
    return re.sub(
        r'\s+', ' ',
        string.replace(
            '\xa0', ' ').replace(  # &nbsp;
            '\n', ' ').replace(
            '\t', ' ').strip()
    )


def on_exception_return(to_return):
    """
    On unpredicted exception return `to_return` provided in the decorator.
    Still raise some specific errors (as NotImplementedError listed here)

    This is needed due to not being able to predict what elements can be missing
    from the DOM and not being able to foresee all the possible erorrs from bs4
    """
    def decorate(decorated_function):
        @wraps(decorated_function)
        def wrap(*args, **kwargs):
            try:
                result = decorated_function(*args, **kwargs)
                return result
            except NotImplementedError as e:
                raise e
            except Exception:
                return to_return
        return wrap
    return decorate
