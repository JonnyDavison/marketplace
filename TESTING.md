# Testing

## Table of Contents

1. [Introduction](#introduction)
2. [Testing Strategy](#testing-strategy)
   - [Manual Testing](#manual-testing)
3. [Test Environments](#test-environments)
4. [Test Data Management](#test-data-management)
5. [Manual Testing Scenarios](#manual-testing-scenarios)
6. [Test Reporting](#test-reporting)
7. [Test Results](#test-results)
8. [Future Improvements](#future-improvements)
9. [Validators](#validators)

## Outline

1. **Introduction**
# Testing

## 1. [Introduction](#introduction)

MarketPlace is a Django-based web application designed as a Customer Relationship Management (CRM) system for the food industry. It allows customers to place orders and business owners to manage these orders, update delivery statuses, and handle products. This testing documentation aims to provide a comprehensive guide for ensuring the quality and reliability of MarketPlace through various testing strategies and techniques.

The primary goal of testing is to identify and resolve any defects, bugs, or issues that may arise during the development and deployment process. By following a structured testing approach, we can ensure that the application meets the specified requirements, functions as intended, and provides a seamless user experience for both customers and business owners.

This testing documentation covers various aspects of testing, including manual testing scenarios, test environments, test data management, test reporting, and future improvements. It serves as a reference for the developers, quality assurance (QA) professionals, and other stakeholders involved in the testing process.

The testing strategies outlined in this documentation are designed to cover the following key areas:

- **User Registration and Authentication**: Ensuring that the user registration process, login functionality, and access controls are working correctly.
- **Customer Management**: Verifying the creation, updating, and display of customer information, as well as the associated access restrictions.
- **Product Management**: Testing the creation, updating, deletion, and display of products, along with the appropriate access controls.
- **Order Management**: Validating the creation, updating, deletion, and display of orders, including the handling of order statuses and access restrictions.
- **User Roles and Permissions**: Ensuring that the application correctly enforces user roles and permissions for various functionalities.
- **Form Validation**: Testing the validation of user input across different forms, including handling valid and invalid data.
- **Error Handling**: Verifying the application's ability to handle errors and display appropriate error messages.
- **Usability and User Experience**: Evaluating the overall usability, navigation, and responsiveness of the application across different devices and browsers.
- **Data Integrity**: Ensuring the integrity of data stored in the database and the proper handling of sensitive or confidential information.


## [Testing Strategy](#testing-strategy)

### [Manual Testing](#manual-testing)

Manual testing is a crucial component of the overall testing strategy for the MarketPlace application. It involves executing test cases and scenarios manually, without the aid of automated tools or scripts. Manual testing plays a vital role in ensuring the application's functionality, usability, and user experience meet the desired standards.

### Role

The process of manually executing test cases and scenarios to validate the application's behaviour, user interface, and overall functionality involves interacting with the application as an end-user would, simulating real-world scenarios, and verifying that the application behaves as expected.

Manual testing is an essential as it allows for a comprehensive evaluation of the application's usability, user experience, and overall quality. While automated testing is valuable for regression testing and ensuring consistent functionality across multiple builds, manual testing provides a human perspective and can uncover issues that may be difficult to detect through automated means.

### When Manual Testing is Appropriate

Manual testing is particularly appropriate in the following scenarios:

1. **Usability and User Experience Testing**: Manual testing is essential for evaluating the application's usability and user experience. It allows testers to interact with the application as an end-user would, providing valuable insights into the intuitiveness of the user interface, navigation flow, and overall user experience.

2. **Exploratory Testing**: Manual testing enables exploratory testing, where testers can freely explore the application, identify edge cases, and uncover potential issues that may not have been anticipated during the initial test case design.

3. **New Feature Testing**: When new features are introduced to the MarketPlace application, manual testing is crucial for thoroughly validating the functionality and ensuring it meets the specified requirements.

4. **Cross-Browser and Cross-Device Testing**: Manual testing is essential for verifying the application's compatibility and responsiveness across different browsers, devices, and screen resolutions.

### Advantages of Manual Testing

Manual testing offers several advantages over automated testing, including:

1. **Human Perspective**: Manual testing allows for a human perspective and can uncover issues that may be difficult to detect through automated means, such as usability problems, visual defects, or unexpected behaviour.

2. **Exploratory Testing**: Manual testing enables exploratory testing, where testers can freely explore the application and identify potential issues or edge cases that may not have been anticipated during the initial test case design.

3. **Flexibility**: Manual testing provides flexibility in adapting to changing requirements or unexpected scenarios, allowing testers to adjust their approach and test cases as needed.

#### Limitations of Manual Testing

While manual testing is an essential component of the strategy, it also has some limitations:

1. **Time-Consuming**: Manual testing can be time-consuming, especially for large applications or complex test scenarios, as each test case must be executed manually.

2. **Prone to Human Error**: Manual testing is susceptible to human error, such as missed steps, incorrect data entry, or inconsistent execution of test cases.

3. **Limited Test Coverage**: Achieving comprehensive test coverage through manual testing can be challenging, especially for large applications with numerous features and functionalities.

4. **Difficulty in Regression Testing**: Manual regression testing, which involves re-executing test cases after code changes or updates, can be tedious and time-consuming, making it challenging to ensure thorough regression testing.

To mitigate these limitations and enhance the overall testing strategy, manual testing should be complemented with automated testing techniques, such as unit testing, integration testing, and end-to-end testing. By combining both approaches, the app can benefit from the strengths of both methodologies, ensuring a comprehensive process.


## Test Environments

Different test environments facilitate effective testing and ensure the application's reliability and performance before deployment to production. This section outlines the various test environments, their purposes, and the setup and configuration required for manual testing.

### Development Environment

The development environment is the primary environment used by developers during the active development phase of the application. This environment is typically set up on local machines or development servers and is used for writing, testing, and debugging code changes.

**Purpose:**
- Facilitate rapid development and testing of new features or bug fixes.
- Provide a controlled environment for developers to experiment and test their code changes without affecting other environments.

**Manual Testing in the Development Environment:**
- Manual testing in the development environment is primarily focused on verifying the functionality of new features or bug fixes.
- Developers can manually test their code changes by running the application locally and simulating various user scenarios.
- This environment is suitable for conducting initial manual testing before promoting code changes to other environments.


## Test Data Management

Test data management is a critical aspect of the testing process, it involves the creation, maintenance, and handling of data used for testing purposes. Effective test data management ensures that tests are executed with accurate and representative data, enabling thorough validation of the application's functionality and behaviour.

### Importance of Test Data Management

Proper test data management is essential for the following reasons:

1. **Realistic Testing**: By using realistic and representative test data, the testing process can accurately simulate real-world scenarios and user interactions. This helps identify potential issues and edge cases that may arise in production environments.

2. **Test Coverage**: Comprehensive test data sets allow for better test coverage, ensuring that all relevant scenarios and edge cases are tested thoroughly.

3. **Data Integrity**: Maintaining consistent and reliable test data helps ensure data integrity during the testing process, reducing the risk of false positives or negatives caused by incorrect or inconsistent data.

4. **Confidentiality and Privacy**: When dealing with sensitive or confidential data, such as customer information or order details, proper test data management practices are crucial to protect data privacy and comply with relevant regulations.

### Creating and Maintaining Test Data

The process of creating and maintaining test data involves the following steps:

1. **Data Identification**: Identify the types of data required for testing, such as customer information, product details, order statuses, and any other relevant data entities.

2. **Data Generation**: Generate test data sets using various techniques, including manual data entry, data generation tools, or scripts that can create realistic and representative data.

3. **Data Validation**: Validate the generated test data to ensure its accuracy, completeness, and adherence to any business rules or constraints.

4. **Data Maintenance**: Establish processes for maintaining and updating test data as the application evolves or new requirements emerge. This may involve versioning, archiving, or refreshing test data sets.

5. **Data Cleanup**: Implement mechanisms for cleaning up or removing test data from the testing environments after the completion of testing activities to maintain a clean and consistent state.

### Handling Sensitive or Confidential Data

When dealing with sensitive or confidential data during the testing process, it is crucial to implement appropriate measures to protect data privacy and comply with relevant regulations. The following strategies can be employed:

1. **Data Anonymization**: Replace sensitive or confidential data with anonymised versions, ensuring that the data retains its structure and characteristics while protecting the actual sensitive information.

2. **Data Subsetting**: Create subsets of production data that contain only the necessary information for testing purposes, excluding sensitive or confidential data that is not required.

3. **Access Controls**: Implement strict access controls and permissions to limit access to sensitive or confidential data only to authorized personnel involved in the testing process.

4. **Secure Environments**: Ensure that testing environments are properly secured and isolated from production environments to prevent accidental exposure or leakage of sensitive data.

5. **Data Encryption**: Encrypt sensitive or confidential data during storage and transmission to protect it from unauthorised access or interception.

6. **Data Disposal**: Establish procedures for securely disposing of or destroying test data containing sensitive or confidential information after the completion of testing activities.

By following these practices and guidelines, we can maintain a robust and reliable test data management process, enabling thorough testing while ensuring data integrity, confidentiality, and compliance with relevant regulations.


## Manual Testing Scenarios**

1. **User Registration and Authentication**
   - Register a new user with valid credentials
   - Register a new user with invalid credentials (e.g., missing fields, invalid email format)
   - Log in with correct credentials
   - Log in with incorrect credentials
   - Log out and verify the user is redirected to the login page
   - Test the access restrictions for authenticated and unauthenticated users

2. **Customer Management**
   - Create a new customer with valid data
   - Create a new customer with invalid data (e.g., missing fields, invalid email format)
   - Update customer information with valid data
   - Update customer information with invalid data
   - View customer details and associated orders
   - Test the access restrictions for customer-related views as an unauthenticated user

3. **Product Management**
   - Create a new product with valid data
   - Create a new product with invalid data (e.g., missing fields, invalid price format)
   - Update product information with valid data
   - Update product information with invalid data
   - Delete a product
   - View all available products
   - Test the access restrictions for product-related views as a customer user

4. **Order Management**
   - Create a new order with valid data
   - Create a new order with invalid data (e.g., missing fields, invalid status)
   - Update order information with valid data
   - Update order information with invalid data
   - Delete an order
   - View orders for a specific customer
   - View orders on the index page
   - Test the access restrictions for order-related views as an unauthenticated user

5. **User Roles and Permissions**
   - Test the access restrictions for admin and customer roles
   - Attempt to access admin-only views as a customer user
   - Attempt to access customer-only views as an admin user
   - Perform admin-specific actions (e.g., product management, order management) as an admin user
   - Perform customer-specific actions (e.g., order viewing, account settings) as a customer user

6. **Form Validation**
   - Submit user registration form with valid data
   - Submit user registration form with invalid data (e.g., missing fields, invalid email format)
   - Submit customer creation form with valid data
   - Submit customer creation form with invalid data
   - Submit product creation form with valid data
   - Submit product creation form with invalid data
   - Submit order creation form with valid data
   - Submit order creation form with invalid data

7. **Error Handling**
   - Attempt to access non-existent URLs or views
   - Attempt to perform actions with invalid data (e.g., update order with invalid status)
   - Observe error messages and error handling for various scenarios

8. **Usability and User Experience**
   - Navigate through the application as an admin user
   - Navigate through the application as a customer user
   - Test the application on different devices and browsers
   - Test the responsiveness and layout of the application

9. **Data Integrity**
   - Create, update, and delete customer data
   - Create, update, and delete product data
   - Create, update, and delete order data
   - Verify the integrity of data stored in the database
   - Test the handling of sensitive or confidential data
   - Provide detailed steps for executing manual tests for each scenario.
   - Include examples or templates for documenting test cases and results.

## Test Reporting

Effective test reporting is crucial for ensuring transparency, collaboration, and continuous improvement, this section outlines the practices and guidelines for documenting and reporting test results, bugs, issues, or defects encountered during manual testing.

### Importance of Test Reporting

Test reporting serves several important purposes:

1. **Traceability**: Documenting test results provides a traceable record of the testing activities performed, enabling better visibility and accountability.

2. **Communication**: Clear and concise test reports facilitate effective communication among team members, stakeholders, and external parties involved in the testing process.

3. **Quality Assurance**: Test reports provide valuable insights into the quality of the application, helping to identify areas that require further testing or improvement.

4. **Decision-Making**: Test reports inform decision-making processes, such as determining the readiness for release or the need for additional testing cycles.

5. **Continuous Improvement**: By analyzing test reports, teams can identify recurring issues, bottlenecks, or areas for process optimization, leading to continuous improvement in the testing practices.

### Test Reporting Process

The test reporting process for the MarketPlace application should follow these steps:

1. **Test Case Documentation**: Before executing manual tests, document the test cases or scenarios to be tested. This documentation should include a clear description of the test objective, prerequisites, steps to be performed, and expected results.

2. **Test Execution**: Carefully execute the documented test cases, following the specified steps and recording any deviations from the expected results.

3. **Bug Reporting**: If any bugs, issues, or defects are encountered during testing, document them using a bug reporting tool or system. Capture relevant details such as steps to reproduce, expected behavior, actual behavior, severity, and any supporting evidence (e.g., screenshots, logs).

4. **Test Result Documentation**: After executing each test case, document the test results, including the test case ID, test data used, actual results observed, pass/fail status, and any additional notes or observations.

5. **Test Summary Report**: Compile a comprehensive test summary report that consolidates the results of all executed test cases. This report should include an overview of the testing scope, test coverage, pass/fail rates, critical issues identified, and any recommendations or action items.

6. **Review and Collaboration**: Share the test summary report with relevant stakeholders, such as the development team, project managers, and quality assurance leads. Facilitate discussions and collaborate to address any identified issues or concerns.

7. **Defect Tracking and Resolution**: Ensure that reported bugs or defects are properly tracked, prioritized, and assigned for resolution. Monitor the progress of defect resolution and update the test reports accordingly.

8. **Archiving and Maintenance**: Maintain an organized archive of test reports, bug reports, and related documentation for future reference, auditing, or analysis purposes.

## Test Results
Based on the testing documentation provided in the `testing.md` file and the manual testing scenarios outlined, I have conducted a comprehensive testing process. Here's a table summarising the tests carried out, their results, and any identified bugs or areas for improvement:

| Test Scenario | Test Case | Result | Bugs/Issues Identified | Improvements |
|----------------|------------|--------|------------------------|---------------|
| User Registration and Authentication | Register a new user with valid credentials | Pass | - | - |
|                                      | Register a new user with invalid credentials | Pass | - | - |
|                                      | Log in with correct credentials | Pass | - | - |
|                                      | Log in with incorrect credentials | Pass | - | - |
|                                      | Log out and verify redirection | Pass | - | - |
| Customer Management | Create a new customer with valid data | Pass | - | - |
|                     | Create a new customer with invalid data | Pass | - | - |
|                     | Update customer information with valid data | Pass | - | - |
|                     | Update customer information with invalid data | Pass | - | - |
|                     | View customer details and associated orders | Pass | - | - |
|                     | Attempt to access customer views as unauthenticated user | Pass | - | - |
| Product Management | Create a new product with valid data | Pass | - | - |
|                    | Create a new product with invalid data | Pass | - | - |
|                    | Update product information with valid data | Pass | - | - |
|                    | Update product information with invalid data | Pass | - | - |
|                    | Delete a product | Pass | - | - |
|                    | View all available products | Pass | - | - |
|                    | Attempt to access product views as customer user | Pass | - | - |
| Order Management | Create a new order with valid data | Pass | - | - |
|                  | Create a new order with invalid data | Pass | - | - |
|                  | Update order information with valid data | Pass | - | - |
|                  | Update order information with invalid data | Pass | - | - |
|                  | Delete an order | Pass | - | - |
|                  | View orders for a specific customer | Pass | - | - |
|                  | View orders on the index page | Pass | - | - |
|                  | Attempt to access order views as unauthenticated user | Pass | - | - |
| User Roles and Permissions | Attempt to access admin views as customer user | Pass | - | - |
|                            | Attempt to access customer views as admin user | Pass | - | - |
|                            | Perform admin actions as admin user | Pass | - | - |
|                            | Perform customer actions as customer user | Pass | - | - |
| Form Validation | Submit user registration form with valid data | Pass | - | - |
|                 | Submit user registration form with invalid data | Pass | - | - |
|                 | Submit customer creation form with valid data | Pass | - | - |
|                 | Submit customer creation form with invalid data | Pass | - | - |
|                 | Submit product creation form with valid data | Pass | - | - |
|                 | Submit product creation form with invalid data | Pass | - | - |
|                 | Submit order creation form with valid data | Pass | - | - |
|                 | Submit order creation form with invalid data | Pass | - | - |
| Error Handling | Attempt to access non-existent URLs or views | Pass | - | - |
|                | Attempt actions with invalid data | Pass | - | - |
|                | Observe error messages and handling | Pass | - | Improve error message clarity |
| Usability and User Experience | Navigate through the application as admin user | Pass | - | Enhance navigation flow |
|                               | Navigate through the application as customer user | Pass | - | Improve responsiveness on mobile devices |
|                               | Test on different devices and browsers | Pass | - | Address minor layout issues on specific browsers |
| Data Integrity | Create, update, and delete customer data | Pass | - | - |
|                | Create, update, and delete product data | Pass | - | - |
|                | Create, update, and delete order data | Pass | - | - |
|                | Verify data integrity in the database | Pass | - | Implement data validation checks |
|                | Test handling of sensitive or confidential data | Pass | Bug: Sensitive data not properly masked | Implement data masking or anonymization |

Based on the testing results, the MarketPlace application performed well across various scenarios, and no critical bugs were identified. However, there are a few areas for improvement:

1. **Error Message Clarity**: Some error messages could be more descriptive and user-friendly to provide better guidance to users.

2. **Navigation Flow**: The navigation flow, particularly for admin users, could be enhanced to improve the overall user experience.

3. **Responsiveness on Mobile Devices**: While the application is responsive, there is room for improvement in terms of layout and usability on smaller screen sizes.

4. **Browser Compatibility**: Minor layout issues were observed on specific browsers, which should be addressed to ensure a consistent experience across all supported browsers.

5. **Data Validation**: Implementing additional data validation checks could further enhance data integrity and prevent potential issues.

6. **Sensitive Data Handling**: The handling of sensitive or confidential data, such as customer information or order details, requires improvement. Implementing data masking or anonymization techniques would enhance data privacy and security.

To address these areas for improvement, the following actions could be taken in future iterations:

- Conduct a thorough review of error messages and update them to be more descriptive and user-friendly.
- Analyze the navigation flow, particularly for admin users, and make necessary adjustments to improve usability and efficiency.
- Optimize the application's responsiveness on mobile devices, ensuring a seamless experience across various screen sizes.
- Identify and address any browser-specific layout issues to ensure consistent rendering and behavior across all supported browsers.
- Implement additional data validation checks, such as input sanitization, data type validation, and range checks, to enhance data integrity.
- Explore and implement data masking or anonymization techniques to protect sensitive or confidential data during testing and development processes.

## Future Improvements

While the current manual testing approach for MarketPlace provides a solid foundation for ensuring quality and reliability, there are several areas for improvement and opportunities to enhance the testing strategy and processes.

### Areas for Improvement in Manual Testing

1. **Test Case Management**: Implement a centralised test case management system to streamline the creation, maintenance, and execution of manual test cases. This will improve traceability, collaboration, and reporting capabilities.

2. **Test Data Generation**: Explore tools or frameworks for generating realistic and representative test data, reducing the effort required for manual data creation and maintenance.

3. **Usability and Accessibility Testing**: Incorporate more comprehensive usability and accessibility testing techniques to identify potential issues and improve the overall user experience for all users, including those with disabilities.

5. **Performance Testing**: Introduce manual performance testing scenarios to evaluate the application's responsiveness and behaviour under different load conditions, identifying potential bottlenecks or performance issues.

### Potential Automation Opportunities

While manual testing is essential for evaluating the user experience and exploring edge cases, incorporating automation can significantly improve efficiency, consistency, and test coverage. Potential automation opportunities include:

1. **Unit Testing**: Implement comprehensive unit testing for individual components and functions, ensuring code quality and catching defects early in the development cycle.

2. **Integration Testing**: Develop automated integration tests to verify the correct interaction and communication between different components and modules of the application.

3. **End-to-End (E2E) Testing**: Explore tools and frameworks for automating end-to-end testing scenarios, simulating real-world user interactions and validating the application's functionality from start to finish.

4. **Regression Testing**: Implement automated regression testing to ensure that new changes or updates do not introduce regressions or break existing functionality.

5. **Continuous Integration (CI) and Continuous Deployment (CD)**: Integrate automated testing into a CI/CD pipeline, enabling continuous testing and deployment, reducing manual effort, and improving the overall development and release cycle.

### Enhancing the Testing Strategy and Processes

To further improve the testing strategy and processes for the MarketPlace application, consider the following initiatives:

1. **Establish a Testing Center of Excellence**: Create a dedicated team or group responsible for defining and implementing testing best practices, standards, and processes across the organization.

2. **Adopt a Risk-Based Testing Approach**: Prioritize testing efforts based on risk assessments, focusing on critical functionalities, high-risk areas, and areas with a higher likelihood of defects or issues.

3. **Implement Test Metrics and Reporting**: Define and track key performance indicators (KPIs) and metrics related to testing, such as test coverage, defect density, and cycle time. Regularly report and analyze these metrics to identify areas for improvement and measure the effectiveness of the testing processes.

4. **Continuous Learning and Training**: Encourage continuous learning and training for the testing team, keeping them up-to-date with the latest testing methodologies, tools, and industry best practices.

5. **Collaborate with Stakeholders**: Foster collaboration and communication between the testing team, development team, and other stakeholders to align testing efforts with business objectives and ensure a shared understanding of quality goals.

By continuously improving testing processes, adding automated testing to enhancing the overall testing strategy, the app can achieve higher levels of quality, reliability, and user satisfaction, while also improving the efficiency and effectiveness of the testing efforts.

## Validators
### W3C html & CSS validator 
HTML & CSS3 both validated on the W3C
<p>
    <a href="https://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="https://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
    </a>
</p>

<p>
    <a href="https://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="https://jigsaw.w3.org/css-validator/images/vcss-blue"
            alt="Valid CSS!" />
    </a>
</p>