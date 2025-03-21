# No Data Sign

**Technical Name:** NoDataSign

**Category:** Reporting

**Default Value:** "-1"

**Impact Level:** Medium

**Description:**

The `NoDataSign` parameter is utilized within the Pathlock Cloud GRC platform to designate a specific symbol or text identifier that is displayed in reports where data fields have no value or are considered null. This identifier aids in distinguishing between fields that have been intentionally left blank, vs. those that do not have any data available.

**Business Impact:**

Implementing a recognizable `NoDataSign` enhances report clarity for users, ensuring that stakeholders can easily interpret instances of no data within the context of security, risk, and compliance reporting. This clarity supports better decision-making processes and ensures accurate audit trails.

**Technical Impact when configured:**

When `NoDataSign` is configured, report fields that yield a value of zero or do not contain any data will display the specified sign. This configuration directly impacts how information is presented in user interfaces related to reporting and analytics, providing explicit visibility into data unavailability.

**Examples Scenario:**

- In a compliance report detailing user actions within certain applications, some columns might not have applicable data for every user. Utilizing the `NoDataSign` can indicate to the compliance officer reviewing the report that no actions were recorded or applicable, as opposed to erroneously assuming missing data.

**Related Settings:**

- `NoDaysGoBackFor`

**Best Practices:** 

- **configure when:** Implementing or updating reports within the Pathlock Cloud GRC platform to provide clear differentiation between fields with no data and those intentionally left blank.
  
- **avoid when:** Information on data absence is irrelevant or might clutter report readability.