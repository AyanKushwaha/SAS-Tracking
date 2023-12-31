package com.sas.interbids.validator;

import com.jeppesen.carmen.crewweb.interbids.customization.api.BidData;
import com.jeppesen.carmen.crewweb.interbids.validation.ValidationDataSet;
import com.jeppesen.carmen.crewweb.interbids.validation.ValidatorResult;
import com.jeppesen.jcms.crewweb.common.util.CWDateTime;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.mockito.Mock;
import org.mockito.runners.MockitoJUnitRunner;

import java.util.ArrayList;

import static com.jeppesen.jcms.crewweb.common.util.CWTimeRange.HOURS;
import static com.jeppesen.jcms.crewweb.common.util.CWTimeRange.MINUTES;
import static com.sas.interbids.validator.TimeOffBidSeparationPeriodValidator.MAXIMUM_ALLOWED_BID_DURATION_IN_HOURS;
import static org.mockito.Matchers.any;
import static org.mockito.Matchers.anyListOf;
import static org.mockito.Matchers.anyString;
import static org.mockito.Mockito.*;

@RunWith(MockitoJUnitRunner.class)
public class TimeOffBidSeparationPeriodValidatorMaximumAllowedDurationExceededTest {

    TimeOffBidSeparationPeriodValidator validator = new TimeOffBidSeparationPeriodValidator();

    @Mock BidData bidData;
    @Mock ValidatorResult result;
    @Mock ValidationDataSet validationDataSet;

    @Test
    public void validateOnUserCreateTest() {

        final CWDateTime startDateTime = CWDateTime.create(2017, 11, 1);

        when(bidData.getType())
                .thenReturn("time_off");
        when(bidData.getStartDate())
                .thenReturn(startDateTime);
        when(bidData.getEndDate())
                .thenReturn(startDateTime.plus(MAXIMUM_ALLOWED_BID_DURATION_IN_HOURS, HOURS)
                                         .plus(1, MINUTES));

        when(validationDataSet.getOtherBidsInSameBidGroupAs(any(BidData.class)))
                .thenReturn(new ArrayList<BidData>());

        validator.validateOnUserCreate(bidData, result, validationDataSet, null);

        verify(result, times(1))
                .addValidationError(anyString(), anyListOf(String.class));
    }
}
