**Excel Matrix Max Number Of Chars To Set Row Height**

**Technical Name:** ExcelMatrix_MaxNumberOfCharsToSetRowHight

**Category:** Reporting

**Default Value:** Not Provided

**Impact Level:** Medium

**Description:**

This parameter controls the maximum number of characters in a cell within an Excel Matrix report that triggers an automatic adjustment of the row height, aiming to make the content fully visible without manual resizing.

**Business Impact:**

Improves readability and presentation of Excel Matrix reports by dynamically adjusting row heights based on cell content length. This ensures that critical information is not obscured, which is vital for stakeholders reviewing compliance, risk assessments, and audit reports.

**Technical Impact when configured:**

When set, this parameter directly influences the layout of generated Excel Matrix reports. It determines to what extent cell content length will automatically modify row heights, potentially leading to more pages but enhanced readability.

**Examples Scenario:**

- **Scenario:** Generating a Risk Assessment Report
    - **Given:** The Excel Matrix Max Number Of Chars To Set Row Height is configured to 100 characters.
    - **When:** A cell within the report contains a risk description of 150 characters.
    - **Then:** The row height for this specific row is automatically adjusted to accommodate the full risk description, making it fully visible without the need for manual adjustments.

**Related Settings:** ExcelMatrix_EnableFreezePanes

**Best Practices:** 

- **Configure when:**
    - Detailed reports with lengthy descriptions are common, necessitating dynamic adjustments to ensure all content is visible.
    - Reports are intended for print, where manual resizing is not feasible.
- **Avoid when:**
    - Conciseness is preferred over detailed descriptions in reports.
    - Extra page length resulting from adjusted row heights could become an issue.