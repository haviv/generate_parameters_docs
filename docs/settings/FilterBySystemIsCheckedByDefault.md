**Technical Name:** FilterBySystemIsCheckedByDefault

**Category:** Configuration

**Default Value:** False

**Impact Level:** Medium

**Description:** This parameter controls whether the system filter option is checked by default in the Pathlock Cloud GRC platform's user interface. It specifically relates to components where filtering data by system is an available functionality.

**Business Impact:** Enabling this parameter by default can streamline the user experience by automatically applying a common filter, potentially reducing the time users spend configuring reports or views within the platform. However, it may also lead to confusion or oversight if users are unaware that this filter is applied automatically.

**Technical Impact when configured:** When enabled, this setting automatically applies a filter based on the system, affecting how data is displayed or processed in the reports or UI components. It may reduce the initial data load, leading to faster access times for filtered information but could restrict the visibility of data across different systems unless manually adjusted.

**Examples Scenario:** If an organization primarily operates within a single system and wishes to ensure that all user interactions with the platform's reporting or monitoring tools are focused on this system, enabling this parameter would automatically apply this common filter, streamlining their workflow.

**Related Settings:** 

- `ShowFilterBySystem`: Determines if the system filter option is available to be applied.
- `EnableModernStyle`: When false, this setting might affect the visibility or applicability of the FilterBySystemIsCheckedByDefault, based on UI constraints.

**Best Practices:** 

- **configure when** the organization's GRC activities are concentrated on a single or primary system, to streamline the user experience.
  
- **avoid when** the organization requires frequent cross-system analysis and reporting, to prevent automatic filtering from obscuring necessary data visibility.