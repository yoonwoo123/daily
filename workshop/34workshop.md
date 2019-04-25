# 34workshop

```python
from django.views.decorators.http import require_POST, require_http_methods

@require_http_methods=(['GET', 'POST'])
def create(request):

	if request.method == "POST":
        board_form = BoardForm(request.POST)
        if board_form.is_valid():
            board = board_form.save()
            return redirect(board)
    else:
        board_form = BoardForm()
    context = {'board_form': board_form}
    return render(request, 'boards/form.html', context)

@require_POST
def delete(request, board_pk):
    if request.method == "POST":
        board = get_object_or_404(Board, pk=board_pk)
        board.delete()
        return redirect('boards:index')
```



