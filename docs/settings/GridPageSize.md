# Grid Page Size

**Technical Name:** GridPageSize

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:** 

The Grid Page Size parameter dictates the number of records displayed on a single page within data grids throughout the Pathlock Cloud GRC platform. Adjusting this parameter allows users to customize their viewing experience based on personal preference or to accommodate screen size and resolution.

**Business Impact:**

Changing the Grid Page Size affects how data is reviewed and interacted with on the platform. A smaller grid size may improve page load times but require more navigation between pages, while a larger grid size can consolidate data but potentially slow down page rendering. This customization can enhance user efficiency and satisfaction depending on their specific role and tasks.

**Technical Impact when configured:**

Configuring the Grid Page Size impacts server load and the end-user experience. A balance must be struck between operational efficiency and user convenience. Incorrect configurations might result in suboptimal performance or a cumbersome user interface.

**Examples Scenario:**

- **Scenario 1:** A compliance officer needs to review thousands of compliance reports. Setting a larger Grid Page Size allows viewing more entries at once, reducing the need to navigate across multiple pages.
- **Scenario 2:** A system administrator working on a device with a small screen might decrease the Grid Page Size for better readability and navigation within the user interface.

**Related Settings:** 

- ExcelMatrixEnableConditionalFormatting
- EventOnEmployeePositionTitleChange

**Best Practices:** 

- Configure a larger Grid Page Size when working on high-resolution monitors for aggregated data viewing.
- Opt for a smaller Grid Page Size on devices with limited screen real estate or to improve page load performance.
- Regularly reassess Grid Page Size settings to match current operational needs and hardware setups.

