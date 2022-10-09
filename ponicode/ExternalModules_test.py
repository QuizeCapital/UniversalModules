from UniversalModules import ExternalModules
import pytest

class Test_Modulessmartfactor_CompoundedAnnualGrowthRate:
    
    @pytest.fixture()
    def modulessmartfactor(self):
        return ExternalModules.modulesSmartFactor()
    

    def test_compoundedAnnualGrowthRate_1(self, modulessmartfactor):
        result = modulessmartfactor.compoundedAnnualGrowthRate()

