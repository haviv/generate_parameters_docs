# Enable Excel Matrix Text Rotation

**Technical Name:** EnableExcelMatrixTextRotation

**Category:** Reporting

**Default Value:** 

**Impact Level:** Medium

**Description:** 

This parameter allows for the rotation of text within Excel matrices generated in the Pathlock Cloud GRC platform. Specifically, it enables the orientation of cell content to be altered for enhanced readability and presentation in Excel reports.

**Business Impact:** 

Enabling Excel Matrix Text Rotation can significantly improve the visualization of complex data sets, particularly in large reports where identifying trends, risks, or issues within the data quickly is essential. This feature can aid in making data-driven decisions more efficiently by enhancing the report's usability.

**Technical Impact when configured:**

When this parameter is configured, Excel matrices generated will display text within specified cells at a rotated angle. This can help to fit more information onto a single page or make certain sections of data stand out more clearly, without affecting the data's integrity or readability.

**Examples Scenario:**

- **Scenario 1:** An audit report contains a vast number of transactions grouped by various criteria. Utilizing the Enable Excel Matrix Text Rotation allows the headers or specific cells to be rotated, making the report more compact and easier to navigate.
    
- **Scenario 2:** Compliance reports that need to highlight specific risks or compliance issues within a large data set. Rotating text in certain sections can draw attention more effectively than standard formatting options.

**Related Settings:** 

- `EnableCUA`
- `EnableCustomActionForAuthoriz`

**Best Practices:** 

- **Configure when:** Reports contain dense data sets or when presentation clarity can significantly enhance report utility and impact. This is especially useful in compliance and audit scenarios where data insights are critical.
  
- **Avoid when:** Reports are already simple or have minimal data, where rotating text might overcomplicate the presentation or when the audience prefers traditional report formats.