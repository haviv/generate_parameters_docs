**Active Directory Get Users By Mail Page Size**

**Technical Name:** ActiveDirectoryGetUsersByMailPageSize

**Category:** User Management

**Default Value:** Not directly provided in the references

**Impact Level:** Medium

**Description:** This parameter defines the page size for querying Active Directory users based on their email addresses. It dictates the number of user records fetched in a single query when syncing or retrieving user details from Active Directory through email search criteria.

**Business Impact:** Optimizing this parameter can significantly enhance performance when synchronizing large user bases from Active Directory into the Pathlock Cloud GRC platform. It affects the efficiency and speed of data sync operations, directly impacting user management processes and overall system performance.

**Technical Impact when configured:** Proper configuration can reduce the number of server requests during synchronization operations by adjusting the amount of data retrieved per request. This can lead to reduced load on the Active Directory server and improved synchronization speed, which is crucial for maintaining up-to-date user information and ensuring compliance and security policies are applied accurately.

**Examples Scenario:** If an organization has thousands of users in its Active Directory, configuring an optimal value for this parameter can drastically cut down the time required for each sync operation. For example, setting a larger page size can be beneficial for organizations with high-speed network connections between the Pathlock Cloud GRC platform and their Active Directory server, whereas smaller sizes might be better for slower networks to avoid timeouts or data fetch issues.

**Related Settings:** While specific related settings were not provided in the code references, settings like ActiveDirectorySecondaryProviderCustomDomains and ActiveDirectorySecondaryProviderUsername may influence or be influenced by this parameter in user synchronization contexts.

**Best Practices:** Configure when you have a clear understanding of your network capabilities and the average size of the user data payload. Avoid using extremely large values without testing, as this might lead to performance degradation or timeouts during data synchronization processes. It's advisable to start with the default value and adjust as needed based on actual sync performance and network capacity.