import ko from knockout;
import arches from arches;
import CIIMIntegrationDashboardTemplate from 'templates/views/components/plugins/ciim_integration_dashboard.htm';

const CIIMIntegrationDashboardViewModel = function() {
    const self = this;
};

export default ko.components.register('ciim_integration_dashboard', {
    viewModel: CIIMIntegrationDashboardViewModel,
    template: defaultReportTemplate,
});