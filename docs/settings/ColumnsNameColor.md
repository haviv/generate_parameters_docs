# MS Excel headers background color:

**Technical Name:** ColumnsNameColor

**Category:** Reporting

**Default Value:** System.Drawing.Color (specific color not provided in the code references)

**Impact Level:** Medium

**Description:** 

The `ColumnsNameColor` parameter controls the background color of column headers in Excel reports generated within the Pathlock Cloud GRC platform. This setting is applied when exporting reports or matrices, enhancing readability and visual organization.

**Business Impact:**

Adjusting the `ColumnsNameColor` can improve the distinguishability of report sections, aiding stakeholders in quickly identifying key data points. This is particularly beneficial for lengthy reports or when presenting to executives who require swift data absorption.

**Technical Impact when configured:**

Once set, the `ColumnsNameColor` parameter ensures that all generated Excel reports have headers with the specified background color. This uniformity aids in maintaining brand consistency and improves the overall aesthetics of exported reports.

**Examples Scenario:**

If the corporate branding colors include a specific shade of blue, setting `ColumnsNameColor` to this color will ensure that all Excel report headers match the corporate branding, reinforcing the company's identity in presentations and documentation.

**Related Settings:** CommonSettings.Default.ExcelMatrix_EnableConditionalFormating

**Best Practices:** 

- **Configure when**:
  - You want to align report aesthetics with corporate branding.
  - There's a need to enhance report readability and data sectioning.
  
- **Avoid when**:
  - Default settings suffice for the report's audience and purpose.
  - Color choices could hinder readability due to poor contrast with text colors.