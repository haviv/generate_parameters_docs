# Disable Impact Column Style

**Technical Name:** DisableImpactColumnStyle

**Category:** Reporting

**Default Value:** Not explicitly mentioned in the provided references

**Impact Level:** Medium

**Description:**

This setting controls the appearance of the impact column in reports. When enabled, it disables custom styling options for the impact column, potentially resulting in a more standard, homogeneous look across reports.

**Business Impact:**

Adjusting this parameter can influence how easily report readers can prioritize and understand the risk or impact information conveyed in reports. A disabled impact column style might make the reports look more consistent but could also reduce the effectiveness of visual cues that highlight critical information.

**Technical Impact when configured:**

Configuring this parameter to `true` removes custom CSS styling from the impact column in reports, affecting how information is visually represented. This could lead to a more simplified presentation but might also obscure nuances that custom styling can highlight.

**Examples Scenario:**

A company wishes to standardize the appearance of their reports across different departments to ensure that all reports have a uniform look. By disabling custom styling on the impact column, they can achieve a more cohesive presentation style across reports, aiding in readability and consistency.

**Related Settings:**

- `DisableAnalyticalViews`

**Best Practices:** configure when consistency and standardization in report presentation are more critical than visual cues for prioritization. Avoid when the impact or risk needs to be immediately noticeable and differentiated through styling.