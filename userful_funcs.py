import matplotlib.pyplot as plt

def plot_1D_data(ax, x, y, yerr=None, label=None, fmt='.', attrs={}, clear_plot=True, frameon=True, markerscale=1, **kwargs):
    """
    Plots data on the given Axes object with optional error bars and attributes.
    Parameters:
        ax (matplotlib.axes.Axes): The axes on which to plot the data.
        x (array-like): The x data.
        y (array-like): The y data.
        yerr (array-like, optional): The error bars for the y data. Defaults to None.
        label (str, optional): The label for the data series. Defaults to None.
        fmt (str, optional): The format string for the data points. Defaults to '.'.
        attrs (dict, optional): A dictionary of attributes to set on the axes. Defaults to {}.
        clear_plot (bool, optional): Whether to clear the plot before plotting. Defaults to True.
        **kwargs: Additional keyword arguments passed to `ax.errorbar`.
    Returns:
        None
    Usage example:
        plot_data(ax, x, y, yerr=y_err, label='Data', fmt='o-', attrs=dict(xscale='linear', yscale='log', xlabel='x', ylabel='y', title='Example Plot'))
    """
    if clear_plot:
        ax.cla()
        
    ax.errorbar(x, y, yerr=yerr, fmt=fmt, label=label, **kwargs)
    ax.set(**attrs)
    if label is not None:
        ax.legend(frameon=frameon, markerscale=markerscale)
        

def plot_imshow(ax, data, attrs={}, cax=None, cb_label=None, cb_fontsize=14, clear=True, **kwargs):
    """
    Displays an image on the given Axes object with optional colorbar and attributes.
    Parameters:
        ax (matplotlib.axes.Axes): The axes on which to display the image.
        data (array-like): The image data.
        attrs (dict): A dictionary of attributes to set on the axes.
        cax (matplotlib.axes.Axes, optional): The axes on which to draw the colorbar. Defaults to None.
        cb_label (str, optional): The label for the colorbar. Defaults to None.
        cb_fontsize (int, optional): The font size for the colorbar label. Defaults to 14.
        clear (bool, optional): Whether to clear the axes before displaying the image. Defaults to True.
        **kwargs: Additional keyword arguments passed to `ax.imshow`.
    Returns:
        None
    Usage example:
        plot_imshow(ax, data, attrs=dict(xlabel='x', ylabel='y', title='Example Image'), cax=cax, cb_label='Colorbar Label', cb_fontsize=14)
    """
    if clear:
        ax.clear()  # Clear the axes if clear is True
        
    i1 = ax.imshow(data, **kwargs)  # Display the image data
    ax.set(**attrs)  # Set the attributes on the axes
    ax.grid(False)  # Disable the grid
    
    if cax is not None:
        cb = plt.colorbar(i1, cax=cax, use_gridspec=True)  # Create a colorbar if cax is provided
        cb.set_label(cb_label, fontsize=cb_fontsize)  # Set the colorbar label and font size
