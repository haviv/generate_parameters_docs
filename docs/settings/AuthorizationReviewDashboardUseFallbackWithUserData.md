# Authorization Review Dashboard Use Fallback With User Data

**Technical Name:** AuthorizationReviewDashboardUseFallbackWithUserData

**Category:** User Management

**Default Value:** False

**Impact Level:** Medium

**Description:**

The `AuthorizationReviewDashboardUseFallbackWithUserData` parameter controls whether the Authorization Review Dashboard should use fallback mechanisms to display user data when primary data sources are unavailable. It ensures continuity in user management and oversight processes by allowing the use of alternative data.

**Business Impact:**

Enabling this parameter ensures that even in the event of primary data source failures, user authorization reviews can continue without interruption. This supports organizational compliance and security policies by maintaining access oversight under all circumstances.

**Technical Impact when configured:**

When enabled, this setting activates secondary data retrieval strategies within the Pathlock Cloud GRC platform. This means that if the usual methods for gathering user data for authorization reviews fail, the system will attempt to retrieve necessary information through pre-defined fallback options.

**Examples Scenario:**

- **Critical Audit Preparation:** During a critical audit period, the primary data source for user information becomes inaccessible. Enabling `AuthorizationReviewDashboardUseFallbackWithUserData` allows the organization to proceed with the authorization review process using fallback user data, ensuring that the audit can be completed on time without compromising on the thoroughness of the review process.

**Related Settings:**

- `AuthorizationReviewTakeFullNameFromUserRecord`

**Best Practices:** 

- **Configure when:** You have multiple sources of user data and want to ensure continuity in authorization review processes, especially during data source outages.
  
- **Avoid when:** All user data is stored in highly reliable systems with little to no downtime, or when fallback data sources may not be up to date, thus risking inaccurate authorization reviews.