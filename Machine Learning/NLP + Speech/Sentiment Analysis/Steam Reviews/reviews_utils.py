URL = """https://steamcommunity.com/app/730/reviews/?browsefilter=
mostrecent&snr=1_5_100010_&p=1&filterLanguage=english
"""

# Styling function
def highlight_mismatch(column):
    """
    Highlights cells depending on the polarity value:
    polarity < 0 = red
    polarity > 0.1 = green
    else = gray

    Returns:
        A list of CSS styles, where "background-color: " is applied 
        depending on the polarity level
    """
    # Compare current column with "Admitted". Returns "True/False" per row
    color_map = []

    for row in column:
        if row < 0:
            color_map.append("background-color: red")
        elif row > 0.1:
            color_map.append("background-color: green")
        else:
            color_map.append("background-color: gray")
    
    return color_map