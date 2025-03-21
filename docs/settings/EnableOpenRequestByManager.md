# Enable Open Request By Manager

**Technical Name:** EnableOpenRequestByManager

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

Enables managers to open access requests on behalf of their team members directly, streamlining the process of granting necessary permissions and resources.

**Business Impact:**

Improving the efficiency of access request processes can significantly reduce the time it takes for team members to gain access to critical systems, ensuring that projects and tasks are not delayed due to administrative procedures. This feature can also help in enforcing proper access control and reducing the risk of unauthorized access, as managers can oversee and request only what's necessary for their team's operations.

**Technical Impact when configured:**

When enabled, this setting allows managers within the organization to initiate access requests in the PathLock Cloud GRC platform on behalf of users they manage. This can lead to a more streamlined workflow, where managers take a proactive role in the access management process, potentially reducing bottlenecks that occur when users initiate requests themselves.

**Examples Scenario:**

A project manager requires their new team member to access certain project management tools and repositories relevant to their role. With this setting enabled, the manager can directly request access for the team member without requiring the team member to navigate the request process themselves, thus speeding up the onboarding process and ensuring the team member can start contributing more quickly.

**Related Settings:**

- UseDefaultRequestSystemId
- OverideRequstSystemId

**Best Practices:** configure when you want to empower managers to manage their team's access needs directly, avoiding when there is a concern about managers potentially requesting inappropriate access levels for their team members.