from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext



############### TEMPLATES ###############
from copy import deepcopy

def deep_merge(a, b):
    '''recursively merges dict's. not just simple a['key'] = b['key'], if
    both a and b have a key who's value is a dict then dict_merge is called
    on both values and the result stored in the returned dictionary.'''
    if not isinstance(b, dict):
        return b
    result = deepcopy(a)
    for k, v in b.iteritems():
        if k in result and isinstance(result[k], dict):
                result[k] = deep_merge(result[k], v)
        else:
            result[k] = deepcopy(v)
    return result


G_TEMPLATE = {'widget' :
                 {'required': '<div class="required">*</div>'
                 }
}

G_TEMPLATE = deep_merge(G_TEMPLATE,
{'widget' :
                           {'input':
                              {'default' :
                                 '\n \
<div class="<!--OUTER_CLASS-->" style="<!--OUTER_STYLE-->" id="<!--OUTER_ID-->">\n \
   <div class="<!--INNER_CLASS-->" style="<!--INNER_STYLE-->">\n \
      <input <!--EVENT_ATTRIBUTES--> <!--READONLY--> type="<!--INPUT_TYPE-->" class="<!--INPUT_CLASS-->" style="<!--INPUT_STYLE-->" id="<!--ID-->" name="<!--NAME-->" title="<!--TITLE-->" value="<!--VALUE-->" maxlength="<!--MAX_LENGTH-->">\n \
   </div>\n \
</div>\n \
<!--REQUIRED-->'
                              }
                           }
                        })

G_TEMPLATE = deep_merge(G_TEMPLATE,
                        {'widget' :
                           {'input':
                              {'search' :
                                 '\n \
<div class="<!--OUTER_CLASS-->" style="<!--OUTER_STYLE-->" onclick="<!--OUTER_ACTION-->">\n \
   <div class="<!--INNER_CLASS-->" style="<!--INNER_STYLE-->">\n \
      <input <!--READONLY--> <!--EVENT_ATTRIBUTES--> type="text" class="<!--INPUT_CLASS-->" style="<!--INPUT_STYLE-->" id="<!--ID-->" name="<!--NAME-->" title="<!--TITLE-->" value="<!--VALUE-->" maxlength="<!--MAX_LENGTH-->">\n \
   </div>\n \
   <div class="widget-search-arrow <!--ARROW_EXTRA_CLASS-->"  onclick="<!--ARROW_ACTION-->"></div>\n \
   <!--MAGNIFIER-->\n \
   <div id="<!--ID-->_results" class="widget-search-drilldown" style="">\n \
      <div class="widget-search-content"><!--SEARCH_FORM--></div>\n \
   </div>\n \
</div>'
                              }
                           }
                        })

G_TEMPLATE = deep_merge(G_TEMPLATE,
                        {'widget' :
                           {'radio':
                              {'default' :
                                 '\n \
<input type="radio" class="<!--INPUT_CLASS-->" style="<!--INPUT_STYLE-->" id="<!--ID-->" name="<!--NAME-->" title="<!--TITLE-->" value="<!--VALUE-->" onclick="<!--ONCLICK-->" <!--CHECKED-->>\n \
<!--REQUIRED-->'
                              }
                           }
                        })

G_TEMPLATE = deep_merge(G_TEMPLATE,
                        {'widget' :
                           {'checkbox':
                              {'default' :
                                 '\n \
<input type="checkbox" class="<!--INPUT_CLASS-->" style="<!--INPUT_STYLE-->" id="<!--ID-->" name="<!--NAME-->" value="<!--VALUE-->" onclick="<!--ONCLICK-->" <!--CHECKED-->  <!--DISABLED-->>\n \
<!--REQUIRED-->'
                              }
                           }
                        })

G_TEMPLATE = deep_merge(G_TEMPLATE,
                        {'widget' :
                           {'selectbox_nostyle':
                              {'wrapper' :
                                 '<select <!--DISABLED_FLG--> class="<!--CLASS-->" id="<!--ID-->" style="<!--STYLE-->" name="<!--NAME-->" <!--MULTIPLE--> size="<!--SIZE-->" onchange="<!--ONCHANGE-->" <!--ATTRIBUTES-->><!--OPTIONS--></select> <!--REQUIRED-->'
                              }
                           }
                        })

G_TEMPLATE = deep_merge(G_TEMPLATE,
                        {'widget' :
                           {'selectbox':
                              {'wrapper' :
                                 '\n \
<div class="<!--OUTER_CLASS-->" style="<!--OUTER_STYLE-->" onclick="<!--OUTER_ACTION-->">\n \
   <div class="<!--INNER_CLASS-->" style="<!--INNER_STYLE-->">\n \
      <select border="0" <!--DISABLED_FLG--> class="<!--CLASS-->" id="<!--ID-->" style="<!--STYLE-->" name="<!--NAME-->" <!--MULTIPLE--> size="<!--SIZE-->" onchange="<!--ONCHANGE-->" <!--ATTRIBUTES-->><!--OPTIONS--></select>\n \
   </div>\n \
</div>\n \
<!--REQUIRED-->'
                              }
                           }
                        })

G_TEMPLATE = deep_merge(G_TEMPLATE,
                        {'widget' :
                           {'selectbox':
                              {'option' :
                                 '<option value="<!--VALUE-->" onclick="<!--ONCLICK-->" <!--SELECTED-->><!--CONTENT--></option>'
                              }
                           }
                        })

G_TEMPLATE = deep_merge(G_TEMPLATE,
                        {'widget' :
                           {'selectbox':
                              {'option_showid' :
                                 '<option value="<!--VALUE-->" onclick="<!--ONCLICK-->" <!--SELECTED-->><!--CONTENT--> (<!--VALUE-->)</option>'
                              }
                           }
                        })

G_TEMPLATE = deep_merge(G_TEMPLATE,
                        {'widget' :
                           {'selectbox':
                              {'option_showid_left' :
                                 '<option value="<!--VALUE-->" onclick="<!--ONCLICK-->" <!--SELECTED-->>(<!--VALUE-->) <!--CONTENT--></option>'
                              }
                           }
                        })

G_TEMPLATE = deep_merge(G_TEMPLATE,
                        {'widget' :
                           {'selectbox':
                              {'initial' :
                                 '<option value="<!--VALUE-->" onclick="<!--ONCLICK-->" <!--SELECTED-->><!--CONTENT--></option>'
                              }
                           }
                        })

G_TEMPLATE = deep_merge(G_TEMPLATE,
                        {'widget' :
                           {'selectbox':
                              {'passive' :
                                 '<span class="<!--CLASS-->" id="<!--ID-->" name="<!--NAME-->" size="<!--SIZE-->" <!--ATTRIBUTES-->><!--OPTIONS--></span>'
                              }
                           }
                        })

G_TEMPLATE = deep_merge(G_TEMPLATE,
                        {'widget' :
                           {'selectfreeflow':
                              {'wrapper' :
                                 '\n \
<div class="<!--OUTER_CLASS-->" style="<!--OUTER_STYLE-->" onclick="<!--OUTER_ACTION-->">\n \
   <div class="<!--INNER_CLASS-->" style="<!--INNER_STYLE-->">\n \
      <!--SELECT_ONE_TEXT-->\n \
   </div>\n \
   <div class="widget-select-freeflow-arrow <!--ARROW_EXTRA_CLASS-->" style="" onclick="<!--ARROW_ACTION-->"></div>\n \
   <div id="select_freeflow_<!--ID-->" class="widget-select-freeflow-drilldown">\n \
      <ul class="widget-select-freeflow-content">\n \
         <!--OPTIONS-->\n \
      </ul>\n \
   </div>\n \
</div>'
                              }
                           }
                        })

G_TEMPLATE = deep_merge(G_TEMPLATE,
                        {'widget' :
                           {'selectfreeflow':
                              {'option' :
                                 '\n \
<li onclick="<!--ONCLICK-->" class="<!--SELECTED-->">\n \
   <input type="hidden" name="select_free_option_name<!--NAME-->[]" name="select_option_<!--NAME-->_id_<!--COUNTER-->" value="<!--VALUE-->">\n \
   <!--CONTENT-->\n \
</li>'
                              }
                           }
                        })

G_TEMPLATE = deep_merge(G_TEMPLATE,
                        {'widget' :
                           {'button':
                              {'default' :
                                 '\n \
<!--FRM_SUBMIT-->\n \
<a class="<!--BUTTON_CLASS-->" style="<!--BUTTON_STYLE-->" onclick="<!--BUTTON_ONCLICK-->" onmouseover="<!--MOUSEOVER-->" onmouseout="<!--MOUSEOUT-->" name="<!--NAME-->" id="<!--ID-->">\n \
   <!--BUTTON_LABEL-->\n \
</a>'
                              }
                           }
                        })

G_TEMPLATE = deep_merge(G_TEMPLATE,
                        {'widget' :
                           {'container':
                              {'row' :
                                 '<tr><!--CONTENT--></tr>'
                              }
                           }
                        })

G_TEMPLATE = deep_merge(G_TEMPLATE,
                        {'widget' :
                           {'container':
                              {'col' :
                                 {'pre_text' :
                                    '<td colspan="<!--COL_SPAN-->" id="<!--ID-->" class="<!--CLASS-->"><div class="container-label"><!--PRE_TEXT--></div> <!--CONTENT--></td>'
                                 }
                              }
                           }
                        })

G_TEMPLATE = deep_merge(G_TEMPLATE,
                        {'widget' :
                           {'container':
                              {'col' :
                                 {'standard' :
                                    '<td colspan="<!--COL_SPAN-->" id="<!--ID-->" class="<!--CLASS-->"><!--CONTENT--></td>'
                                 }
                              }
                           }
                        })

G_TEMPLATE = deep_merge(G_TEMPLATE,
                        {'widget' :
                           {'container':
                              {'wrapper' :
                                 '<form method="post" id="<!--FORM_ID-->"><table class="<!--OUTER_CLASS-->" id="<!--OUTER_ID-->"><!--CONTENT--></table>'
                              }
                           }
                        })


############### UTILS ###############
import json
import hashlib
import urllib

def not_empty(var):
    return len(var) > 0

def empty(var):
    return len(var) == 0

def widget_list_header(request, include_jquery=True):

    if include_jquery==True:
        include_jquery = '<script src="//ajax.googleapis.com/ajax/libs/jquery/2.0.0/jquery.min.js"></script>'
    else:
        include_jquery = ''

    if 'mod_wsgi.application_group' in request.META:
        asset_path = '/static_widget_list/'
        dev        = ''
    else:
        asset_path = '/static/'
        dev        = '_dev'

    #See instructions on why we have two copies of the same CSS for use with apache WGSI and local dev to load paths
    return '\n' + include_jquery + '\n\
     <script src="' + asset_path + 'assets/javascripts/widget_list.js" type="text/javascript"></script> \n\
     <link  href="' + asset_path + 'assets/stylesheets/widgets'     + dev + '.css" media="all" rel="stylesheet" type="text/css"/>\n\
     <link  href="' + asset_path + 'assets/stylesheets/widget_list' + dev + '.css" media="all" rel="stylesheet" type="text/css"/>\n\
     '

def fill(tags = {}, template = ''):
    for k in tags:
        if tags[k] == False or tags[k] == True:
            tags[k] = ''
        template = template.replace(str(k),str(tags[k]))
    return template

def json_encode(arr, return_string = False):
    if return_string:
        print json.dumps(arr)
    else:
        return json.dumps(arr)


def build_query_string(args):
    q = []
    for k in args:
        #@todo: add array support
        #if tags[k].class.name == 'Hash':
        #    q << {k => v}.to_params
        #else:
        q.append(str(k) + '=' + urllib.quote(urllib.unquote(str(args[k]))))
    return '&'.join(q)

def build_url(page='',args = {}, append_get=False, get_vars={}):
      qs = build_query_string(args)
      getvartmp = ''
      if append_get and get_vars:
          getvartmp = build_query_string(get_vars)
      out = ''
      if page.find('?'):
          out = page + '?' + qs + '&' + getvartmp
      else:
          out = page + qs + '&' + getvartmp
      return out


def test_all_utils(request):

    test = 'adsfasdf <!--NAME-->  <!--NAME--> '
    a = fill({'<!--NAME-->':'dave'}, test)

    output_final = ''
    output_final += "JsonEncode\n<br/>\n<br/>"
    a = {}
    a['asdfasdf'] = 'asfd'
    a['test'] = 1234
    a[2153125] = None
    output_final += json_encode(a)

    output_final += "\n<br/>\n<br/>BuildQueryString\n<br/>\n<br/>"
    a = { }
    a['asdfasdf'] = 'asdf asdfj ajskdfhasdf'
    a['dave'] = 'a)(J#(*J@T2p2kfasdfa fas %20fj ajskdfhasdf'
    output_final += build_query_string(a)


    output_final += "\n<br/>\n<br/>BuildUrl\n<br/>\n<br/>"
    output_final += build_url('page.php?',a,True,request.REQUEST)

    output_final += "\n<br/>\n<br/>BuildUrl\n<br/>\n<br/>"
    output_final += build_url('page.php?',a,False,request.REQUEST)

    return output_final


############### WIDGETS ###############

def populate_items(list,items):
    if list != None:
        for k in list:
            if k in list:
                items[k] = list[k]
    return items

# WidgetCheck
def widget_check(list={}):

    items = {
                 'name'                 : '',
                 'id'                   : '',
                 'value'                : '',
                 'width'                : '',
                 'disabled'             : False,
                 'hidden'               : False,
                 'required'             : False,
                 'checked'              : False,
                 'title'                : '',
                 'class'                : '',
                 'onclick'              : '',
                 'input_style'          : '',
                 'input_class'          : '',
                 'template'             : '',
            }

    items['template_required'] = G_TEMPLATE['widget']['required']
    items['template']          = G_TEMPLATE['widget']['checkbox']['default']

    items = populate_items(list,items)

    if items['required'] == False:
        items['template_required'] = ''

    if items['checked'] == True:
        items['checked'] = 'checked'

    if len(items['class']) > 0:
        items['input_class'] = items['class']

    if items['disabled']:
        items['disabled'] = 'disabled'
    else:
        items['disabled'] = ''

    if items['hidden'] == True:
        items['style'] += ' display:none'

    pieces = {
        '<!--INPUT_CLASS-->' : items['input_class'],
        '<!--INPUT_STYLE-->' : items['input_style'],
        '<!--ID-->'          : items['id'],
        '<!--NAME-->'        : items['name'],
        '<!--TITLE-->'       : items['title'],
        '<!--ONCLICK-->'     : items['onclick'],
        '<!--VALUE-->'       : items['value'],
        '<!--REQUIRED-->'    : items['template_required'],
        '<!--CHECKED-->'     : items['checked'],
        '<!--VALUE-->'       : items['value'],
        '<!--DISABLED-->'    : items['disabled']
    }

    return fill(pieces, items['template'])

def widget_input(list={}):
    items = {
        'name'              : '',
        'id'                : '',
        'outer_id'          : '',
        'value'             : '',
        'input_type'        : 'text', #hidden
        'width'             : '150',
        'readonly'          : False,
        'disabled'          : False,
        'hidden'            : False,
        'required'          : False,
        'list-search'       : False,
        'max_length'        : '',
        'events'            : {},
        'title'             : '',
        'add_class'         : '',
        'class'             : 'inputOuter',
        'inner_class'       : 'inputInner',
        'outer_onclick'     : '',
        'style'             : '',
        'inner_style'       : '',
        'input_style'       : '',
        'input_class'       : '',
        'template'          : '',
        'search_ahead'      : {},
        'search_form'       : '',
        'search_handle'     : '',
        'arrow_extra_class' : '',
        'icon_extra_class'  : '',
        'arrow_action'      : ''
    }

    items['template_required'] = G_TEMPLATE['widget']['required']

    items['template']          = G_TEMPLATE['widget']['input']['default']

    items = populate_items(list,items)

    iconAction     = ''
    outerAction    = ''
    onkeyup        = ''

    if not_empty(items['outer_onclick']):
        outerAction = items['outer_onclick']

    if not_empty(items['search_ahead']):
        # Search Ahead Input
        #
        items['template'] = G_TEMPLATE['widget']['input']['search']

    fill_tmp = {}
    if items['list-search'] == True:
        fill_tmp['<!--MAGNIFIER-->'] = '<div class="widget-search-magnifier <!--ICON_EXTRA_CLASS-->" style="" onclick="<!--ICON_ACTION-->"></div>'

    items['template'] = fill(fill_tmp,items['template'])

    if not_empty(items['search_ahead']['search_form']):
        if empty(items['arrow_action']):
            items['arrow_action'] = "ToggleAdvancedSearch(this)"

    if 'icon_action' in items['search_ahead']:
        iconAction = items['search_ahead']['icon_action']

    if 'events' in items and 'onkeyup' in items['events']:
        keyUp = items['events']['onkeyup'] + ';'
    else:
        keyUp = ''

    if 'onkeyup' in items['search_ahead'] and not_empty(items['search_ahead']['onkeyup']):
        items['events']['onkeyup'] = keyUp + items['search_ahead']['onkeyup']
    else:
        if items['list-search'] == True:
            items['events']['onkeyup'] = keyUp + "SearchWidgetList('{1}', '{0}', this);".format(items['search_ahead']['target'],items['search_ahead']['url'])
        elif 'skip_queue' in items['search_ahead'] and not_empty(items['search_ahead']['skip_queue']):
            items['events']['onkeyup'] = keyUp +    "WidgetInputSearchAhead('{1}', '{0}', this);".format(items['search_ahead']['target'],items['search_ahead']['url'])
        else:
            items['events']['onkeyup'] = keyUp + "WidgetInputSearchAheadQueue('{1}', '{0}', this);".format(items['search_ahead']['target'],items['search_ahead']['url'])

    if not_empty(items['events']['onkeyup']):
        iconAction = items['events']['onkeyup']

    if 'onclick' in items['search_ahead']:
        items['events']['onclick'] = items['search_ahead']['onclick']

    items['input_class'] += ' search-ahead'

    # Modify the width a bit to compensate for the search icon
    #
    items['width'] = int(items['width']) - 30

    # Build advanced searching
    #
    if not_empty(items['search_ahead']['search_form']):
        if items['list-search'] == True:
            items['arrow_extra_class'] += ' widget-search-arrow-advanced'
        else:
            items['arrow_extra_class'] += ' widget-search-arrow-advanced-no-search'
        items['icon_extra_class']     += ' widget-search-magnifier-advanced'
        items['input_class']                += ' search-ahead-advanced'

    #
    #    Mandatory For outer boundary and IE7
    #
    #    @todo should be css MW 5/2012
    #
    items['style'] += "width:{0}px".format(items['width'])

    if items['required'] == False:
        items['template_required'] = ''

    if items['disabled'] == True:
        items['input_class'] += ' disabled'

    if not_empty(items['add_class']):
        items['class'] += ' ' + items['add_class']

    if items['hidden'] == True:
        items['style'] += ' display:none'

    items['event_attributes'] = ''
#    if not_empty(items['events'])
#
#        items['events'].each { |event,action|
#            items['event_attributes'] += ' ' + event + '="' + action + '"' + ' '
#        }
#    end

    if ('search_form' in items['search_ahead']) == False:
        items['search_ahead']['search_form'] = ''

    if items['readonly'] == True:
        readonly = 'readonly'
    else:
        readonly = ''

    return fill({
                            '<!--READONLY-->'             : readonly,
                            '<!--OUTER_ID-->'             : items['outer_id'],
                            '<!--OUTER_CLASS-->'          : items['class'],
                            '<!--OUTER_STYLE-->'          : items['style'],
                            '<!--INNER_CLASS-->'          : items['inner_class'],
                            '<!--INNER_STYLE-->'          : items['inner_style'],
                            '<!--INPUT_CLASS-->'          : items['input_class'],
                            '<!--INPUT_STYLE-->'          : items['input_style'],
                            '<!--ID-->'                   : items['id'],
                            '<!--NAME-->'                 : items['name'],
                            '<!--TITLE-->'                : items['title'],
                            '<!--MAX_LENGTH-->'           : items['max_length'],
                            '<!--ONKEYUP-->'              : onkeyup,
                            '<!--SEARCH_FORM-->'          : items['search_ahead']['search_form'],
                            '<!--VALUE-->'                : items['value'],
                            '<!--REQUIRED-->'             : items['template_required'],
                            '<!--ICON_ACTION-->'          : iconAction,
                            '<!--OUTER_ACTION-->'         : outerAction,
                            '<!--EVENT_ATTRIBUTES-->'     : items['event_attributes'],
                            '<!--INPUT_TYPE-->'           : items['input_type'],
                            '<!--ARROW_EXTRA_CLASS-->'    : items['arrow_extra_class'],
                            '<!--ARROW_ACTION-->'         : items['arrow_action'],
                            '<!--ICON_EXTRA_CLASS-->'     : items['icon_extra_class']
                            } ,
                            items['template']
    )


def widget_button(text='', list={}, small=False):
    items = {
        'label'            : text,
        'name'             : '',
        'id'               : '',
        'url'              : '',
        'link'             : '',                #alias of url
        'href'             : '',                #alias of url
        'page'             : '',
        'parameters'       : False,
        'style'            : 'display:inline-block;cursor:pointer;',
        'frmSubmit'        : '',                #this option adds hidden frmbutton
        'submit'           : '',
        'args'             : {},
        'class'            : 'btn',             #Always stays the same
        'innerClass'       : 'info',            #.primary(blue) .info(light-blue) .success(green) .danger(red) .disabled(light grey) .default(grey)
        'passive'          : False,
        'function'         : 'ButtonLinkPost',
        'onclick'          : '',
        'onmouseover'      : '',
        'onmouseout'       : '',
        'template'         : ''
    }

    items = populate_items(list,items)

    if 'submit' in items and not_empty(items['submit']):
        items['onclick'] = "ButtonFormPost('{0}');".format(list['submit'])

    if empty(items['template']):
        theClass = ''
        if small:
            theClass = items['class'] + " small " + items['innerClass']
        elif not_empty(items['class']):
            theClass = items['class'] + " " + items['innerClass']

        items['template'] = G_TEMPLATE['widget']['button']['default']
    else:
        theClass = items['class']

    if empty(items['url']) and not_empty(items['page']):
        items['url'] = build_url(items['page'], items['args'])

    if not_empty(items['href']) and empty(items['onclick']):
        items['onclick'] = items['function'] + "('{0}')".format(items['href'])

    if not_empty(items['url']) and empty(items['onclick']):
        items['onclick'] = items['function'] + "('{0}')".format(items['url'])

    if not_empty(items['link']) and empty(items['onclick']):
        items['onclick'] = items['function'] + "('{0}')".format(items['link'])

    if items['parameters'] == True and not_empty(items['args']) and items['args'].__class__.__name__ == 'dict':
        parameters = []

        for k in items['args']:
            parameter = items['args'][k]
            if parameter == 'this' or (parameter.find('function') != -1 and parameter.find('{') and parameter.find('}')):
                parameters.append(str(parameter))
            else:
                tmp = "'" + str(parameter) + "'"
                parameters.append(tmp)
        items['onclick'] = items['function']    +    "(" +    ','.join(parameters) + ")"

    if not_empty(items['frmSubmit']):
        items['frmSubmit'] = "<input type=\"submit\" value=\"\" style=\"position: absolute; float: left; z-index: -1;\"/> "

    return fill({
                                '<!--BUTTON_CLASS-->'       : theClass,
                                '<!--BUTTON_ONCLICK-->'     : items['onclick'].replace('"',"'"),
                                '<!--BUTTON_LABEL-->'       : items['label'],
                                '<!--NAME-->'               : items['name'],
                                '<!--ID-->'                 : items['id'],
                                '<!--BUTTON_STYLE-->'       : items['style'],
                                '<!--BUTTON_CLASS_INNER-->' : items['innerClass'],
                                '<!--MOUSEOVER-->'          : items['onmouseover'],
                                '<!--MOUSEOUT-->'           : items['onmouseout'],
                                '<!--FRM_SUBMIT-->'         : items['frmSubmit'],
                },
                items['template']
    )


def test_all():
    output_final    = ''


    #test submit
    #output_final += widget_button('asfdsaf', {'id':'asdfasdf','submit':'213131'}) + "<br/><br/>"

    #test arguments
    output_final += widget_button('asfdsaf', {'parameters':True,'args':{'dave':'123','dan':'1234'}}) + "<br/><br/>"

    #test arguments with JS func
    output_final += widget_button('asfdsaf', {'parameters':True,'args': {'dave':'function() {    alert(0); } '} } ) + "<br/><br/>"

    #output_final += widget_button('asfdsaf', {'name':'asdfasf', 'id':'asfdasdf', 'parameters':True,'args': {'dave':'function() {    alert(0); } '} }, True) + "<br/><br/>"

    input = {}
    input['list-search'] = True
    input['width']             = '300'
    input['input_class'] = 'info-input'
    input['title']             = 'test search'
    input['id']                    = 'list_search_id_'
    input['name']                = 'list_search_name_'
    input['value']                = 'dave'
    input['class']             = 'inputOuter widget-search-outer -search'
    input['search_ahead']             = {
        'url'                    : 'http://google.com',
        'skip_queue'     : False,
        'target'             : 'test',
        'search_form'    : '',
        'onclick'            : ''
    }
    output_final += widget_input(input) + "<br/><br/>"
    return output_final





def index(request):

    input = {}
    input['list-search']       = True
    input['width']             = '300'
    input['input_class']       = 'info-input'
    input['title']             = 'fasdfasdfsdf'
    input['input_style']       = 'color:blue'
    input['id']                = 'list_search_id_'
    input['name']              = 'list_search_name_'
    input['value']             = 'asfdasd'
    input['class']             = '3234234234'

    output = "<pre>" + repr(request) + test_all_utils(request) + "</pre>" + test_all() + widget_check(input)

    return render_to_response('items/items_home.html',
                              {
                                 'yield'  : output,
                                 'header' : widget_list_header(request),
                              },
                              context_instance=RequestContext(request))
