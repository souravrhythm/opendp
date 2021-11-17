use proc_macro::TokenStream;
use std::collections::HashMap;
use std::iter::FromIterator;

use proc_macro2::{Ident, Span};
use quote::quote;
use syn::{AttributeArgs, ItemFn, Lit, Meta, MetaNameValue, NestedMeta, parse_macro_input, Signature};

macro_rules! extract_variant {
  ($value:expr, $pattern:pat => $extracted_value:expr) => {
    match $value {
      $pattern => $extracted_value,
      _ => panic!("Pattern doesn't match!"),
    }
  };
}

#[proc_macro_attribute]
pub fn generate_ffi(attr: TokenStream, item: TokenStream) -> TokenStream {
    let item_ = item.clone();

    // Parse arguments to the proc-macro
    let mut args = HashMap::<String, String>::from_iter(parse_macro_input!(attr as AttributeArgs)
        .into_iter()
        .map(|arg| {
            let meta = extract_variant!(arg, NestedMeta::Meta(v) => v);
            let MetaNameValue { path, lit, .. } = extract_variant!(meta, Meta::NameValue(v) => v);
            if path.segments.len() != 1 { panic!("Path must be of length 1!") }
            (path.segments[0].ident.to_string(), extract_variant!(lit, Lit::Str(v) => v).value())
        }));

    // Parse the function signature
    let Signature {
        ident, generics: _, inputs: _, output: _, ..
    } = parse_macro_input!(item as ItemFn).sig;

    // Retrieve the base function name and construct the extern fn name
    let ffi_name = Ident::new(
        &*format!("opendp_{}__{}",
                  args.remove(&"module".to_string()).unwrap(),
                  ident.to_string()),
        Span::call_site());

    // Construct the extern fn (in-progress)
    let ffi_func = quote!{
        extern "C" fn #ffi_name() {}
    };

    // current state of the generated function:
    println!("{}", ffi_func);

    // for now, just return the base function as-is, without adding the extern fn
    item_
}