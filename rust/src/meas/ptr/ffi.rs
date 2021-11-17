use std::convert::TryFrom;
use std::hash::Hash;
use std::os::raw::{c_char, c_void};

use num::{Float, One, Zero};

use crate::core::{FfiResult, IntoAnyMeasurementFfiResultExt};
use crate::dist::IntDistance;
use crate::err;
use crate::ffi::any::AnyMeasurement;
use crate::ffi::util::Type;
use crate::meas::make_count_by_ptr;
use crate::samplers::SampleLaplace;
use crate::traits::{CheckNull, InfCast, SaturatingAdd};

#[no_mangle]
pub extern "C" fn opendp_meas__make_count_by_ptr(
    scale: *const c_void,
    threshold: *const c_void,
    TIA: *const c_char,  // atomic type of input key (hashable)
    TOC: *const c_char,  // type of count (float)
) -> FfiResult<*mut AnyMeasurement> {
    fn monomorphize<TIA, TOC>(
        scale: *const c_void, threshold: *const c_void,
    ) -> FfiResult<*mut AnyMeasurement>
        where TIA: 'static + Eq + Hash + Clone + CheckNull,
              TOC: 'static + Float + Zero + One + SaturatingAdd + CheckNull + InfCast<IntDistance> + SampleLaplace {
        let scale = *try_as_ref!(scale as *const TOC);
        let threshold = *try_as_ref!(threshold as *const TOC);
        make_count_by_ptr::<TIA, TOC>(scale, threshold).into_any()
    }
    let TIA = try_!(Type::try_from(TIA));
    let TOC = try_!(Type::try_from(TOC));

    dispatch!(monomorphize, [
        (TIA, @hashable),
        (TOC, @floats)
    ], (scale, threshold))
}
