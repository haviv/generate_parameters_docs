# Cache For Pathlock Roles In Hours

**Technical Name:** CachaForProfileTailorRolesInHours

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter controls the duration in hours for caching the roles within the Pathlock Cloud GRC platform. Caching is utilized to enhance performance by storing role data in memory, reducing the need to frequently query the database for this information.

**Business Impact:**

Proper configuration of this parameter can significantly affect the application's performance and responsiveness. An optimally set cache duration ensures that changes to roles are reflected in a timely manner while still leveraging the benefits of caching for performance efficiency.

**Technical Impact when configured:**

When set, this parameter determines how long role information is stored in the cache before it is refreshed from the database. A shorter duration means the system will query the database more frequently for updates, which may increase the database load but ensures that role changes are quickly applied. Conversely, a longer duration reduces database load by extending the time role information is reused from cache, at the risk of delaying the application of role updates.

**Examples Scenario:**

- **Security Update Delays:** If the cache duration is set too long, a user's change in roles due to a security update may not be applied promptly, potentially allowing access longer than intended.
  
- **Performance Optimization:** In a scenario where role assignments are relatively stable and not subject to frequent changes, a longer cache duration could be configured to reduce database load and improve application performance without significantly impacting data accuracy.

**Related Settings:**

- `SiteMapNodeRoles`: This setting is related as it deals with the caching mechanism for site navigation based on user roles, showing a direct application of caching roles in the system's functionality.

**Best Practices:** 

- **Configure when:** Role assignments are relatively stable, and the impact of delayed role updates is minimal. This approach helps in reducing database load and improving performance.
  
- **Avoid when:** Frequent role changes are common, or immediate application of role updates is critical for security or operational reasons. In such cases, a shorter cache duration or more dynamic role management might be necessary.