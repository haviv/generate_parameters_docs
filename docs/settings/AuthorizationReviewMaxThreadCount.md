# Authorization Review Max Thread Count

**Technical Name:** AuthorizationReviewMaxThreadCount

**Category:** Workflow

**Default Value:**

**Impact Level:** High

**Description:**
The Authorization Review Max Thread Count parameter is designed to control the maximum number of threads used during authorization reviews within the Pathlock Cloud GRC platform. This setting determines how many parallel processes can run during the authorization certification process, affecting the efficiency and speed of these operations.

**Business Impact:**
Adjusting this parameter directly impacts the time taken to complete authorization reviews and certifications, which are crucial for maintaining compliance and ensuring that only authorized users have access to sensitive data and systems. A properly configured thread count can significantly reduce the time needed for these processes, leading to better compliance management and resource utilization.

**Technical Impact when configured:**
When this parameter is configured, it optimizes the performance of the authorization certification processes by balancing the load and enabling the system to handle multiple requests simultaneously without overloading the server. This balance ensures that the system remains responsive and efficient, even during intensive review processes.

**Examples Scenario:**
In a scenario where an organization is undergoing its quarterly compliance audits, adjusting the Authorization Review Max Thread Count to an optimal value can expedite the review of user access rights across various systems. This ensures that any non-compliant or unauthorized access is quickly identified and addressed, thereby minimizing the risk of compliance violations.

**Related Settings:** 

**Applicable Workflows Actions:** 
- AuthoirizationCertificationBO

**Best Practices:** 
- **Configure when:** There is a need to optimize the performance of authorization review processes, especially during peak audit periods or when deploying large-scale changes to user access rights.
- **Avoid when:** The system is already under heavy load or when the optimal configuration has not been determined, to prevent potential performance degradation.