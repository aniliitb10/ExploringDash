# styling.py

class BaseStyle:
    """Base class for common style properties."""

    def __init__(
            self,
            overflow_x=None,
            border=None,
            border_radius=None,
            box_shadow=None,
            text_align=None,
            padding=None,
            font_size=None,
            font_family=None,
            background_color=None,
            color=None,
            font_weight=None,
            border_bottom=None,
    ):
        self.overflow_x = overflow_x
        self.border = border
        self.border_radius = border_radius
        self.box_shadow = box_shadow
        self.text_align = text_align
        self.padding = padding
        self.font_size = font_size
        self.font_family = font_family
        self.background_color = background_color
        self.color = color
        self.font_weight = font_weight
        self.border_bottom = border_bottom

    def generate(self):
        """Generates the style dictionary."""
        style = {
            "overflowX": self.overflow_x,
            "border": self.border,
            "borderRadius": f"{self.border_radius}px" if self.border_radius else None,
            "boxShadow": self.box_shadow,
            "textAlign": self.text_align,
            "padding": self.padding,
            "fontSize": self.font_size,
            "fontFamily": self.font_family,
            "fontWeight": self.font_weight,
        }
        if self.background_color:
            style["backgroundColor"] = self.background_color
        if self.color:
            style["color"] = self.color
        if self.border_bottom:
            style["borderBottom"] = self.border_bottom

        # Remove None values to keep the dictionary clean
        return {key: value for key, value in style.items() if value is not None}


class TableContainerStyle(BaseStyle):
    """Specific style for the table container."""

    def __init__(self):
        super().__init__(
            overflow_x="auto",
            border="1px solid #e7e7e7",
            border_radius=8,
            box_shadow="0 4px 12px rgba(0, 0, 0, 0.1)",
        )


class TableCellStyle(BaseStyle):
    """Specific style for the table cells."""

    def __init__(self):
        super().__init__(
            text_align="left",
            padding="12px",
            font_size="14px",
            font_family="Arial, sans-serif",
            border_bottom="1px solid #e7e7e7",
        )


class TableHeaderStyle(BaseStyle):
    """Specific style for the table headers."""

    def __init__(self):
        super().__init__(
            background_color="#f4f4f4",
            color="#212529",
            font_weight="600",
            text_align="left",
            border_bottom="2px solid #007bff",
        )


class DropDownContainerStyle(BaseStyle):
    """Specific style for the dropdown container."""

    def __init__(self):
        super().__init__(
            border="1px solid #e7e7e7",
            border_radius=8,
            box_shadow="0 4px 8px rgba(0, 0, 0, 0.1)",
            background_color="#f9f9f9",
            padding="10px",
        )


class ResetButtonStyle(BaseStyle):
    """Specific style for the reset button."""

    def __init__(self):
        super().__init__(
            background_color="#007bff",
            color="white",
            font_weight="bold",
            border_radius=5,
            padding="10px 20px",
            box_shadow="0 2px 5px rgba(0, 0, 0, 0.2)",
        )

    def generate(self):
        """Adds custom button-specific properties."""
        style = super().generate()
        style.update({
            "cursor": "pointer",
            "border": "none",
        })
        return style


class FlexRowStyle:
    """Layout style for a row-based flexbox container."""

    def __init__(self):
        self.style = {
            "display": "flex",
            "flexDirection": "row",
            "alignItems": "flex-start",
            "gap": "20px",
        }

    def generate(self):
        return self.style


class PieChartContainerStyle:
    """Specific style for the pie chart container."""

    def __init__(self):
        self.style = {
            "flex": "0.3",
            "marginRight": "20px",
        }

    def generate(self):
        return self.style


class TableWrapperStyle:
    """Specific style for the table wrapper container."""

    def __init__(self):
        self.style = {
            "flex": "0.7",
        }

    def generate(self):
        return self.style