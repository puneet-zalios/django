var date_params = ['dateoc', 'dateexp'];
var addButton = null;
var rowCounter = 0;
var ids = [];

function toggleNot(span) {
    span = $(span);
    var weight = span.getStyle('font-weight');
    var input = span.getElementsByTagName('input')[0];
    if (weight === 'bold') {
	span.setStyle({fontWeight:'normal', color:'gray'});
	input.setAttribute('value', '0');
    } else {
	span.setStyle({fontWeight:'bold', 'color':'red'});
	input.setAttribute('value', '1');
    }
}

function updateRowList() {
    var el = document.getElementById('rowlist');
    el.setAttribute('value', ids.join(','));
}

function addID(id) {
    ids.push(id);
    updateRowList();
}

function removeID(id) {
    var i = ids.indexOf(id);
    ids.splice(i, 1);
    updateRowList();
}

function addRow(rowRef) {
    var row = document.createElement('p');
    row.className = 'searchline';
    row.id = rowCounter.toString();
    rowCounter++;
    addID(row.id);

    row.appendChild(createCatSelect(row.id, row));
    row.appendChild(createNot(row.id));
    row.appendChild(createOpsSelect(row.id, row));
    row.appendChild(createField(row.id));
    row.appendChild(createCaseSensitive(row.id));
    row.appendChild(createAddButton(row));

    var form = document.getElementById('incsearch');

    if (form.getElementsByTagName('p').length != 0) {
	row.appendChild(createDeleteButton(row));
    }

    if (rowRef == null) {
	form.insertBefore(row, document.getElementById('submit'));
    } else {
	for (var i=0; i<form.childNodes.length; i++) {
	    if (form.childNodes[i] == rowRef  
		  && (i+1) < form.childNodes.length) {
		// Since the submit div is last, it should always insert
		form.insertBefore(row, form.childNodes[i+1]);
	    }
	}
    }
}

function createAddButton(row) {
    var plus = createInput(null, 'button', 'plus', '+');
    //    plus.addEventListener('click', function() {addRow(row);}, false);
    Event.observe(plus, 'click', function() {addRow(row);})
    return plus;
}

function removeRow(row) {
    removeID(row.id);
    row.parentNode.removeChild(row);
}

function createDeleteButton(row) {
    var deleteButton = createInput(null, 'button', 'minus', '-');
    var delEvent = function() {
	removeRow(row);
    };
    //    deleteButton.addEventListener('click', delEvent, false);
    Event.observe(deleteButton, 'click', delEvent);
    return deleteButton;
}

function createField(id) {
    var field = createInput(id, 'text', 'field', null);
    return field;
}

function createNot(id) {
    var span = $(document.createElement('span'));
    span.className = 'nottoggle';
    span.setStyle({color:'gray'});
    span.observe('click', function() {
	    toggleNot(span);
	});
    var over = function() {
	span.setStyle({cursor:'pointer'});
    };
    Event.observe(span, 'mouseover', over);
    var off = function() {
	span.setStyle({cursor:'default'});
    };
    span.observe('mouseout', off);
    span.appendChild(document.createTextNode('Not'));
    span.appendChild(createNotInput(id));
    return span;
}

function createCaseSensitive(id) {
    var span = $(document.createElement('span'));
    span.className = 'nottoggle';
    span.setStyle({color:'gray'});
    span.observe('click', function() {
	    toggleNot(span);
	});
    var over = function() {
	span.setStyle({cursor:'pointer'});
    };
    Event.observe(span, 'mouseover', over);
    var off = function() {
	span.setStyle({cursor:'default'});
    };
    span.observe('mouseout', off);
    span.appendChild(document.createTextNode('Aa'));
    span.appendChild(createCSInput(id));
    return span;
}

function createNotInput(id) {
    return createInput(id, 'hidden', 'not', '0');
}

function createCSInput(id) {
    return createInput(id, 'hidden', 'cs', '0');
}

function createInput(id, type, name, value) {
    var input = document.createElement('input');
    if (id) {
	input.id = name + id;
    }
    input.setAttribute('type', type);
    input.setAttribute('name', input.id);
    if (value != null) {
	input.setAttribute('value', value);
    }
    return input;
}

function addDate(row) {
    Calendar.setup(
		   {
		       inputField : 'field'+row.id,
			   ifFormat : '%m/%d/%Y %l:%M %P',
			   showsTime: true,
			   singleClick: true,
			   step: 1,
			   eventName: 'click',
			   timeFormat: '12'
			   });
}

function catEvent(row) {
    return function(option) {
	if (date_params.indexOf(option.getAttribute('value')) != -1) {
	    addDate(row);
	}
    };
}

function createListAdder(field, select) {
    var values = [];
    return function(event) {
	var value = field.getValue();
	if (value != undefined && value !== '' && values.indexOf(value) == -1) {
	    if (select.length == 1 && select.options[0].value == '') {
		select.removeChild(select.options[0]);
	    }
	    values.push(value);
	    var option = createOption([value, value]);
	    option.selected = 'select';
	    select.appendChild(option);
	    select.size = values.length;
	    field.clear();
	    event.stop();
	}
    };
}

function removeInitialText(initial) {
    return function (event) {
	if (this.value == initial) {
	    this.value = '';
	    this.focus();
	    this.stopObserving('mousedown', arguments.callee);
	}
    }
}

function createList(row) {
    var select_div = $(document.createElement('div'));
    select_div.addClassName('field');

    var text_field = row.childNodes[3];
    var id = 'field' + row.getAttribute('id');
    var text_input = $(document.createElement('input'));
    var add_button = $(document.createElement('span'));
    var select = document.createElement('select');
    
    text_input.setAttribute('type', 'text');
    var text_initial = 'Type Here';
    text_input.value = text_initial;
    text_input.observe('mousedown', removeInitialText(text_initial));
    var listAdder = createListAdder(text_input, select);
    text_input.observe('keypress', function(event) {
	    if (event.keyCode == Event.KEY_RETURN) {
		listAdder(event);
	    }
	});
    select_div.appendChild(text_input);

    add_button.appendChild(document.createTextNode('Add'));
    add_button.addClassName('add-list-button');
    add_button.observe('click', listAdder);
    select_div.appendChild(add_button);

    select.setAttribute('id', id);
    select.setAttribute('name', id);
    select.multiple = true;
    select.size = 2;
    select.appendChild(createOption(['', '(No Values)']));
    select_div.appendChild(select);

    row.replaceChild(select_div, text_field);
}

function getField(row) {
    return row.childNodes[3];
}

function opEvent(row) {
    return function(option) {
	if (option.getAttribute('value') == 'in') {
	    createList(row);
	} else {
	    var field = getField(row);
	    if (field.tagName == 'DIV' && field.className == 'field') {
		field.parentNode.replaceChild(createField(row.id), field);
	    }
	}
    }
}

function createCatSelect(id, row) {
    return createSelect(id, 'type', cat_list, catEvent(row));
}

function createOpsSelect(id, row) {
    return createSelect(id, 'op', op_list, opEvent(row));
}

function createSelect(id, name, options, event) {
    var select = document.createElement('select');
    select.id = name + id;
    select.setAttribute('name', select.id);
    for (var i=0; i<options.length; i++) {
	select.appendChild(createOption(options[i]));
    }
    if (event != null) {
	var func = function() {
	    event(select.options[select.selectedIndex]);
	};
	//	select.addEventListener('change', func, false);
	// Event.observe(select, 'change', func);
    $j(select).change(func);
    }
    return select;
}

function createOption(data) {
    var option = document.createElement('option');
    option.setAttribute('value', data[0]);
    option.appendChild(document.createTextNode(data[1]));
    return option;
}

function checkFields(event) {
    
}