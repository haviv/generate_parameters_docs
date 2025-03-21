# Search Using Contains Instead Of Starts With

**Technical Name:** SearchUsingContainsInsteadOfStartsWith

**Category:** Configuration

**Default Value:** N/A

**Impact Level:** Medium

**Description:** This parameter controls the search behavior in specific workflows and reporting features within the Pathlock Cloud GRC platform. When enabled, it modifies the default search operation from a "starts with" approach to a "contains" approach. This adjustment can improve the discovery of records by allowing partial match searches within strings, instead of limiting searches to those starting with the specified query.

**Business Impact:** Adjusting this setting to use "contains" can significantly enhance user experience by making searches more flexible and results more comprehensive, particularly in situations where exact starting strings may not be known. It’s particularly useful in extensive datasets where precise terminology or spelling may vary, improving the efficiency of data retrieval and reporting tasks.

**Technical Impact when configured:** Upon configuration, the system's search logic will shift from returning records that begin with the provided search term to those that include it anywhere in the searchable fields. This change impacts data querying performance and may influence load times for large datasets. Adequate testing should be conducted to balance search flexibility with system performance.

**Examples Scenario:** If the parameter is enabled within the "CompanyEmployeesWithoutUsers_AC" workflow action, searching for an employee using part of their name or ID that's not at the beginning will still yield relevant results. For example, searching for "son" will return "Jackson", "Anderson", or "Sonja", instead of just names starting with "son".

**Related Settings:** N/A

**Best Practices:** 
- **configure when** you are dealing with large datasets, and precise beginning strings are unknown or variable; it's crucial for improving search result accuracy in reports or listings.
- **avoid when** system performance is a concern, especially if large datasets are involved and search efficiency could be significantly impacted by broader search criteria.